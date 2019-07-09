from django.test import TestCase
from django.core.exceptions import ValidationError

from aircraft_registration_field import validators


class ValidatorTest(TestCase):

    def test_valid(self):
        try:
            validators.validate_aircraft_registration_number('F-JAZE')
        except ValidationError:
            self.fail('Raise an unexpected ValidationError')

    def test_invalid(self):
        with self.assertRaises(ValidationError):
            validators.validate_aircraft_registration_number('F-1111')
