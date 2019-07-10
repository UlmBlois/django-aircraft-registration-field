from django.test import TestCase
from django.core.exceptions import ValidationError

from aircraft_registration_field import formfields


class AircraftRegistrationPrefixWidgetTest(TestCase):

    def setUp(self):
        self.field = formfields.AircraftRegistrationField()

    def test_validate_valid(self):
        try:
            self.field.validate('F-JAZE')
        except ValidationError:
            self.fail('Raise an unexpected ValidationError')

    def test_validate_invalid(self):
        with self.assertRaises(ValidationError):
            self.field.validate('F-1111')

    def test_empty_value(self):
        self.assertEqual('', self.field.to_python(''))
        self.assertEqual('', self.field.to_python(None))
