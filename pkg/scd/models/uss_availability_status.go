package models

import (
	"github.com/interuss/dss/pkg/api/v1/scdpb"
	dssmodels "github.com/interuss/dss/pkg/models"
)

// Aggregates constants for uss availability.
const (
	UssAvailabilityStateUnknown UssAvailabilityState = "Unknown"
	UssAvailabilityStateNormal  UssAvailabilityState = "Normal"
	UssAvailabilityStateDown    UssAvailabilityState = "Down"
)

// UssAvailabilityState models the state of an uss availability.
type UssAvailabilityState string

// UssAvailabilityStatus models an uss availability status.
type UssAvailabilityStatus struct {
	ID           dssmodels.ID
	Owner        dssmodels.Manager
	Uss          dssmodels.Manager
	Version      Version
	Availability UssAvailabilityState
}

func (u UssAvailabilityState) String() string {
	return string(u)
}

// ToProto converts the Subscription to its proto API format
func (s *UssAvailabilityStatus) ToProto() (*scdpb.UssAvailabilityStatus, error) {
	result := &scdpb.UssAvailabilityStatus{
		Availability: s.Availability.String(),
		Uss:          s.Uss.String(),
	}
	return result, nil
}
