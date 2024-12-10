from django import forms
from .models import Appointment, TIMESLOT_CHOICES
from treatments.models import Treatment

class AppointmentForm(forms.ModelForm):
    appointment_date = forms.DateField(
        widget=forms.TextInput(attrs={'id': 'datepicker'}),
        label="Select a Date"
    )
    appointment_time = forms.ChoiceField(choices=TIMESLOT_CHOICES, label="Select a Time")

    class Meta:
        model = Appointment
        fields = ["name", "treatment_selected", "appointment_date", "appointment_time", "requests"]