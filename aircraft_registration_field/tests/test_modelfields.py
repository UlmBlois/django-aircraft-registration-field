from django.core.exceptions import ValidationError
from django.test import SimpleTestCase

from aircraft_registration_field import modelfield


class AircraftRegistrationFieldValidationTests(SimpleTestCase):

    def test_raise_error_on_invalid_code(self):
        f = modelfield.AircraftRegistrationField()
        with self.assertRaises(ValidationError):
            f.clean('F-1111', None)
