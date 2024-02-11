from django.forms import ModelForm
from .models import *

class AppointmentForm(ModelForm):
    class Meta:
        model=Appointment
        fields="__all__"