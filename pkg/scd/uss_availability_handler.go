package scd

import (
	"context"
	dsserr "github.com/interuss/dss/pkg/errors"
	dssmodels "github.com/interuss/dss/pkg/models"
	scdmodels "github.com/interuss/dss/pkg/scd/models"
	"github.com/interuss/stacktrace"
)
import "github.com/interuss/dss/pkg/api/v1/scdpb"

func (a *Server) GetUssAvailability(ctx context.Context, request *scdpb.GetUssAvailabilityRequest) (*scdpb.UssAvailabilityStatusResponse, error) {

	ussId, err := dssmodels.ManagerFromString(request.GetUssId())
	if err != nil {
		return nil, stacktrace.NewErrorWithCode(dsserr.BadRequest, "Invalid Uss ID: `%s`", request.GetUssId())
	}

	status, err := (&scdmodels.UssAvailabilityStatus{
		Uss:          dssmodels.Manager(ussId),
		Availability: scdmodels.UssAvailabilityStateUnknown,
	}).ToProto()

	if err != nil {
		return nil, stacktrace.Propagate(err, "Could not convert UssAvailabilityStatus to proto")
	}

	result := &scdpb.UssAvailabilityStatusResponse{
		Status:  status,
		Version: "",
	}

	return result, nil
}

func (a *Server) SetUssAvailability(ctx context.Context, request *scdpb.SetUssAvailabilityRequest) (*scdpb.UssAvailabilityStatusResponse, error) {
	panic("implement me")
}
