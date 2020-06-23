package cockroach

import (
	"context"
	"errors"
	"flag"
	"testing"
	"time"

	"github.com/dpjacques/clockwork"
	"github.com/google/uuid"
	"github.com/interuss/dss/pkg/cockroach"
	"github.com/interuss/dss/pkg/logging"
	dssmodels "github.com/interuss/dss/pkg/models"
	ridmodels "github.com/interuss/dss/pkg/rid/models"
	"github.com/interuss/dss/pkg/rid/repos"
	"github.com/lib/pq"
	"github.com/stretchr/testify/require"
	"golang.org/x/mod/semver"
)

var (
	storeURI  = flag.String("store-uri", "", "URI pointing to a Cockroach node")
	fakeClock = clockwork.NewFakeClock()
	startTime = fakeClock.Now().Add(-time.Minute)
	endTime   = fakeClock.Now().Add(time.Hour)
)

func init() {
	DefaultTimeout = 50 * time.Millisecond
}

func setUpStore(ctx context.Context, t *testing.T) (*Store, func()) {
	if len(*storeURI) == 0 {
		t.Skip()
	}
	// Reset the clock for every test.
	fakeClock = clockwork.NewFakeClock()

	store, err := newStore()
	require.NoError(t, err)
	require.NoError(t, store.Bootstrap(ctx))
	return store, func() {
		require.NoError(t, CleanUp(ctx, store))
		require.NoError(t, store.Close())
	}
}

func newStore() (*Store, error) {
	cdb, err := cockroach.Dial(*storeURI)
	if err != nil {
		return nil, err
	}
	return &Store{
		db:     cdb,
		logger: logging.Logger,
		clock:  fakeClock,
	}, nil
}

// CleanUp drops all required tables from the store, useful for testing.
func CleanUp(ctx context.Context, s *Store) error {
	const query = `
	DROP TABLE IF EXISTS subscriptions;
	DROP TABLE IF EXISTS identification_service_areas;`

	_, err := s.db.ExecContext(ctx, query)
	return err
}

func TestStoreBootstrap(t *testing.T) {
	var (
		ctx                  = context.Background()
		store, tearDownStore = setUpStore(ctx, t)
	)
	require.NotNil(t, store)
	tearDownStore()
}

func TestDatabaseEnsuresBeginsBeforeExpires(t *testing.T) {
	var (
		ctx                  = context.Background()
		store, tearDownStore = setUpStore(ctx, t)
	)
	require.NotNil(t, store)
	defer tearDownStore()

	repo, err := store.Interact(ctx)
	require.NoError(t, err)

	var (
		begins  = time.Now()
		expires = begins.Add(-5 * time.Minute)
	)
	_, err = repo.InsertSubscription(ctx, &ridmodels.Subscription{
		ID:                dssmodels.ID(uuid.New().String()),
		Owner:             "me-myself-and-i",
		URL:               "https://no/place/like/home",
		NotificationIndex: 42,
		StartTime:         &begins,
		EndTime:           &expires,
	})
	require.Error(t, err)
}

func TestTxnRetrier(t *testing.T) {
	var (
		ctx                  = context.Background()
		store, tearDownStore = setUpStore(ctx, t)
	)
	require.NotNil(t, store)
	defer tearDownStore()

	err := store.Transact(ctx, func(repo repos.Repository) error {
		// can query within this
		isa, err := repo.InsertISA(ctx, serviceArea)
		require.NotNil(t, isa)
		return err
	})
	require.NoError(t, err)
	// can query afterwads
	repo, err := store.Interact(ctx)
	require.NoError(t, err)

	isa, err := repo.GetISA(ctx, serviceArea.ID)
	require.NoError(t, err)
	require.NotNil(t, isa)

	// Test the retry happens
	// 20ms, let's see how many retries we get.
	// Using a context ensures we bail out.
	ctx, cancel := context.WithTimeout(ctx, 20*time.Millisecond)
	defer cancel()
	count := 0
	err = store.Transact(ctx, func(repo repos.Repository) error {
		// can query within this
		count++
		// Postgre retryable error
		return &pq.Error{Code: "40001"}
	})
	require.Error(t, err)
	// Ensure it was retried.
	require.Greater(t, count, 1)
}

func TestGetVersion(t *testing.T) {
	var (
		ctx                  = context.Background()
		store, tearDownStore = setUpStore(ctx, t)
	)
	defer tearDownStore()
	version, err := store.GetVersion(ctx)
	require.NoError(t, err)
	require.NoError(t, err)

	// TODO: remove the below checks when we have better schema management
	require.Equal(t, "v2", semver.Major(version))

	_, err = store.db.ExecContext(ctx, `CREATE TABLE IF NOT EXISTS cells_subscriptions (id STRING PRIMARY KEY);`)
	require.NoError(t, err)

	version, err = store.GetVersion(ctx)
	require.NoError(t, err)
	require.Equal(t, "v1", semver.Major(version))

	_, err = store.db.ExecContext(ctx, `DROP TABLE cells_subscriptions;`)
	require.NoError(t, err)

}

func TestTransactor(t *testing.T) {
	var (
		ctx                  = context.Background()
		store, tearDownStore = setUpStore(ctx, t)
	)
	require.NotNil(t, store)
	defer tearDownStore()

	subscription1 := subscriptionsPool[0].input
	subscription2 := subscriptionsPool[1].input

	txnCount := 0
	err := store.Transact(ctx, func(s1 repos.Repository) error {
		// We should get to this retry, then return nothing.
		if txnCount > 0 {
			return errors.New("already failed")
		}
		txnCount++
		err := store.Transact(ctx, func(s2 repos.Repository) error {
			subs, err := s1.SearchSubscriptions(ctx, subscription1.Cells)
			require.NoError(t, err)
			require.Len(t, subs, 0)
			subs, err = s2.SearchSubscriptions(ctx, subscription1.Cells)
			require.Len(t, subs, 0)
			require.NoError(t, err)

			// Tx1 conflicts first
			_, err = s1.InsertSubscription(ctx, subscription1)
			require.NoError(t, err)

			// Tx1 is rolled back, so tx2 can proceed.
			_, err = s2.InsertSubscription(ctx, subscription2)
			require.NoError(t, err)

			return nil
		})
		return err
	})
	require.Error(t, err)

	repo, err := store.Interact(ctx)
	require.NoError(t, err)

	subs, err := repo.SearchSubscriptions(ctx, subscription1.Cells)
	require.NoError(t, err)

	require.Len(t, subs, 1)

	s, err := repo.GetSubscription(ctx, subscription1.ID)
	require.NoError(t, err)
	require.Nil(t, s)

	s, err = repo.GetSubscription(ctx, subscription2.ID)
	require.NoError(t, err)
	require.NotNil(t, s)

}

// Test here for posterity to demonstrate transaction semantics
func TestBasicTxn(t *testing.T) {
	var (
		ctx                  = context.Background()
		store, tearDownStore = setUpStore(ctx, t)
	)
	require.NotNil(t, store)
	defer tearDownStore()

	subscription1 := subscriptionsPool[0].input
	subscription2 := subscriptionsPool[1].input

	tx1, err := store.db.Begin()
	require.NoError(t, err)
	s1 := &repo{
		isaRepo: &isaRepo{
			Queryable: tx1,
			logger:    logging.Logger,
		},
		subscriptionRepo: &subscriptionRepo{
			Queryable: tx1,
			logger:    logging.Logger,
			clock:     DefaultClock,
		},
	}

	tx2, err := store.db.Begin()
	require.NoError(t, err)
	s2 := &repo{
		isaRepo: &isaRepo{
			Queryable: tx2,
			logger:    logging.Logger,
		},
		subscriptionRepo: &subscriptionRepo{
			Queryable: tx2,
			logger:    logging.Logger,
			clock:     DefaultClock,
		},
	}

	subs, err := s1.SearchSubscriptions(ctx, subscription1.Cells)
	require.NoError(t, err)
	require.Len(t, subs, 0)
	subs, err = s2.SearchSubscriptions(ctx, subscription1.Cells)
	require.Len(t, subs, 0)
	require.NoError(t, err)

	// Tx1 conflicts first
	sub, err := s1.InsertSubscription(ctx, subscription1)
	require.NoError(t, err)
	require.NotNil(t, sub)
	// Tx1 is rolled back, so tx2 can proceed.
	_, err = s2.InsertSubscription(ctx, subscription2)
	require.NoError(t, err)

	require.Error(t, tx1.Commit())
	require.NoError(t, tx2.Commit())

	repo, err := store.Interact(ctx)
	require.NoError(t, err)

	subs, err = repo.SearchSubscriptions(ctx, subscription2.Cells)
	require.NoError(t, err)

	require.Len(t, subs, 1)
}
