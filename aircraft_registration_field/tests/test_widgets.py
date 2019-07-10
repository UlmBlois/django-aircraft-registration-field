from django.forms.models import modelform_factory
from django.test import TestCase

from aircraft_registration_field import widgets
from aircraft_registration_field.tests.model import ULM


class AircraftRegistrationPrefixWidgetTest(TestCase):

    def setUp(self):
        self.Form = modelform_factory(ULM, fields=["registration"])

    def test_is_default_widget(self):
        widget = self.Form().fields["registration"].widget
        self.assertTrue(isinstance(
            widget,
            widgets.AircraftRegistrationPrefixWidget))

    def test_decompress(self):
        widget = self.Form().fields["registration"].widget
        decompressed = widget.decompress('F-JAER')
        self.assertEqual(['F-', 'JAER'], decompressed)

    def test_decompress_unknow_prefix(self):
        widget = self.Form().fields["registration"].widget
        decompressed = widget.decompress('EH-JAER')
        self.assertEqual([None, ''], decompressed)

    def test_decompress_empty(self):
        widget = self.Form().fields["registration"].widget
        decompressed = widget.decompress('')
        self.assertEqual([None, ''], decompressed)

    def test_value_from_datadict(self):
        widget = self.Form().fields["registration"].widget
        self.assertEqual(
            widget.value_from_datadict(
                {'registration_0': 'F-', 'registration_1': 'JAER'},
                {}, 'registration'),
            'F-JAER')
        self.assertEqual(
            widget.value_from_datadict(
                {'registration_0': None, 'registration_1': 'JAER'},
                {}, 'registration'),
            'JAER')
        self.assertEqual(
            widget.value_from_datadict(
                {'registration_0': 'F-', 'registration_1': None},
                {}, 'registration'),
            'F-')
