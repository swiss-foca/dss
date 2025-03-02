from faker import Faker
import string
import random
import uuid

from monitoring.monitorlib.rid_automated_testing.injection_api import OperatorLocation


class OperatorFlightDataGenerator:
    """A class to generate fake data detailing operator name, operation name and operator location, it can be customized for locales and locations"""

    def __init__(self):
        self.fake = Faker()

    def generate_serial_number(self):
        return str(uuid.uuid4())

    def generate_registration_number(self, prefix="CHE"):
        registration_number = prefix + "".join(
            random.choices(string.ascii_lowercase + string.digits, k=13)
        )
        return registration_number

    def generate_operation_description(self):
        operation_description = [
            "Electricity Grid Inspection",
            "Wind farm survey",
            "Solar Panel Inspection",
            "Traffic Monitoring",
            "Emergency services / rescue",
            "Delivery operation, see more details at https://deliveryops.com/operation",
            "News recording, live event",
            "Crop spraying / Agricultural Inspection",
        ]
        return random.choice(operation_description)

    def generate_operator_location(self, centroid):
        operator_location = OperatorLocation(lat=centroid.y, lng=centroid.x)
        return operator_location

    def generate_operator_id(self, prefix="OP-"):
        operator_id = prefix + "".join(
            random.choices(string.ascii_lowercase + string.digits, k=8)
        )
        return operator_id

    def generate_company_name(self):
        return self.fake.company()
