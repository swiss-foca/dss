import datetime
from monitoring.monitorlib.auth import make_auth_adapter
from monitoring.monitorlib.infrastructure import DSSTestSession
import json, os
import uuid
from pathlib import Path
from monitoring.monitorlib import fetch
from monitoring.uss_qualifier.utils import FullFlightRecord
from monitoring.uss_qualifier import reports
from monitoring.monitorlib.rid_automated_testing.injection_api import TestFlightDetails, TestFlight, CreateTestParameters, SCOPE_RID_QUALIFIER_INJECT
from monitoring.monitorlib.typing import ImplicitDict
import arrow
import pathlib

from typing import List, Optional
from monitoring.uss_qualifier.utils import RIDQualifierTestConfiguration

class TestBuilder():
    ''' A class to setup the test data and create the objects ready to be submitted to the test harness '''

    def __init__(
            self, test_configuration: RIDQualifierTestConfiguration,
            aircraft_state_files: Optional[list] = None) -> None:
        self.test_configuration = test_configuration
        # Change directory to read the test_definitions folder appropriately
        p = pathlib.Path(__file__).parent.absolute()
        os.chdir(p)

        usses = self.test_configuration.injection_targets

        self.disk_flight_records: List[FullFlightRecord] =[]
        if not aircraft_state_files:
            aircraft_states_directory = Path(
                'test_definitions', test_configuration.locale, 'aircraft_states')
            aircraft_state_files = self.get_aircraft_states(aircraft_states_directory)

            for uss_index, uss in enumerate(usses):
                aircraft_states_path = Path(aircraft_state_files[uss_index])
                with open(aircraft_states_path, 'rb') as generated_rid_state:
                    disk_flight_record = ImplicitDict.parse(json.load(generated_rid_state), FullFlightRecord)
                    self.disk_flight_records.append(disk_flight_record)
        else:
            for uss_index, uss in enumerate(usses):
                generated_rid_state = aircraft_state_files[uss_index]
                disk_flight_record = ImplicitDict.parse(json.loads(generated_rid_state), FullFlightRecord)
                self.disk_flight_records.append(disk_flight_record)


    def get_aircraft_states (self, aircraft_states_directory: Path):

        ''' This method checks if there are tracks in the tracks directory '''

        all_files = os.listdir(aircraft_states_directory)
        files = [os.path.join(aircraft_states_directory,f) for f in all_files if os.path.isfile(os.path.join(aircraft_states_directory, f))]

        if files:
            return files
        else:
            raise ValueError("The there are no tracks in the tracks directory, create tracks first using the flight_data_generator module. ")

    def build_test_payloads(self) -> List[CreateTestParameters]:
        ''' This is the main method to process the test configuration and build RID payload object, maxium of one flight is allocated to each USS. '''

        all_test_payloads = [] # This holds the data that will be deilver

        test_reference_time = arrow.now()
        test_start_time = test_reference_time + self.test_configuration.flight_start_delay.timedelta
        test_start_isoformat = test_start_time.isoformat()

        for state_data_index, flight_record in enumerate(self.disk_flight_records):
            disk_reference_time_raw = flight_record.reference_time
            disk_reference_time = arrow.get(disk_reference_time_raw)

            flight_record.reference_time = test_reference_time.isoformat()

            timestamp_offset = test_start_time - disk_reference_time

            for telemetry_id, flight_telemetry in enumerate(flight_record.states):
                timestamp = arrow.get(flight_telemetry.timestamp) + timestamp_offset
                flight_telemetry.timestamp = timestamp.isoformat()

            test_flight_details = TestFlightDetails(effective_after = test_start_isoformat, details = flight_record.flight_details.rid_details)

            test_flight = TestFlight(
              injection_id=str(uuid.uuid4()),
              telemetry=flight_record.states,
              details_responses=[test_flight_details])

            test_payload = CreateTestParameters(requested_flights=[test_flight])

            all_test_payloads.append(test_payload)

        return all_test_payloads


class TestHarness():
    ''' A class to submit Aircraft RID State to the USS test endpoint '''

    def __init__(self, auth_spec:str, injection_base_url:str):

        auth_adapter = make_auth_adapter(auth_spec)
        self.uss_session = DSSTestSession(injection_base_url, auth_adapter)

    def submit_test(self, payload: CreateTestParameters, test_id: str, setup: reports.Setup) -> None:
        injection_path = '/tests/{}'.format(test_id)

        initiated_at = datetime.datetime.utcnow()
        response = self.uss_session.put(url=injection_path, json=payload, scope=SCOPE_RID_QUALIFIER_INJECT)
        #TODO: Use response to specify flights as actually-injected rather than assuming no modifications
        setup.injections.append(fetch.describe_query(response, initiated_at))

        if response.status_code == 200:
            print("New test with ID %s created" % test_id)

        elif response.status_code == 409:
            raise RuntimeError("Test with ID %s already exists" % test_id)

        elif response.status_code == 404:
            raise RuntimeError("Test with ID %s not submitted, the requested endpoint was not found on the server" % test_id)

        elif response.status_code == 401:
            raise RuntimeError("Test with ID %s not submitted, the access token was not provided in the Authorization header, or the token could not be decoded, or token was invalid" % test_id)

        elif response.status_code == 403:
            raise RuntimeError("Test with ID %s not submitted, the access token was decoded successfully but did not include the appropriate scope" % test_id)

        elif response.status_code == 413:
            raise RuntimeError("Test with ID %s not submitted, the injection payload was too large" % test_id)

        else:
            raise RuntimeError("Test with ID %(test_id)s not submitted, the server returned the following HTTP error code: %(status_code)d %(msg)s" % {'test_id': test_id, 'status_code': response.status_code, 'msg': response.content})
