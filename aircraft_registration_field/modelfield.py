from django.utils.translation import ugettext_lazy as _
from django.db import models

from aircraft_registration_field.validators import validate_aircraft_registration_number
from aircraft_registration_field import formfields


class AircraftRegistrationField(models.CharField):
    default_validators = [validate_aircraft_registration_number]
    description = _("Aicraft registration number")

    def __init__(self, *args, **kwargs):
        # TODO check registration code max_length
        kwargs.setdefault("max_length", 10)
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            "form_class": formfields.AircraftRegistrationField,
            "error_messages": self.error_messages,
        }
        defaults.update(kwargs)
        return super().formfield(**defaults)
