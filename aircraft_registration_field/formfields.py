# from django.core.exceptions import ValidationError
from django.forms.fields import CharField
from django.utils.translation import ugettext_lazy as _

import logging

from aircraft_registration_field.validators import validate_aircraft_registration_number
from aircraft_registration_field.widgets import AircraftRegistrationPrefixWidget

logger = logging.getLogger(__name__)


class AircraftRegistrationField(CharField):
    default_error_messages = {"invalid": _("Enter a valid radio call sign.")}
    default_validators = [validate_aircraft_registration_number]
    widget = AircraftRegistrationPrefixWidget

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def validate(self, value):
        super().validate(value)
        validate_aircraft_registration_number(value)
