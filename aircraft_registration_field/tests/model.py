from django.db import models
from aircraft_registration_field.modelfield import AircraftRegistrationField


class ULM(models.Model):
    registration = AircraftRegistrationField()
