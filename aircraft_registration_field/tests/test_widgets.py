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
        self.assertEquals(['F-', 'JAER'], decompressed)

    def test_decompress_unknow_prefix(self):
        widget = self.Form().fields["registration"].widget
        decompressed = widget.decompress('EH-JAER')
        self.assertEquals([None, ''], decompressed)
