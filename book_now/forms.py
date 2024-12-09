from django import forms
from .models import Appointment, TIMESLOT_CHOICES
from treatments.models import Treatment
from datetime import date

class AppointmentForm(forms.ModelForm):
    appointment_date = forms.DateField(
        widget=forms.TextInput(attrs={
            'id': 'datepicker', 
            'placeholder': 'Select a Date',
        }),
        label="Select a Date"
    )
    appointment_time = forms.ChoiceField(choices=TIMESLOT_CHOICES, label="Select a Time")

    class Meta:
        model = Appointment
        fields = ["name", "treatment_selected", "appointment_date", "appointment_time", "requests"]
    
    def clean_appointment_date(self):
        selected_date = self.cleaned_data.get("appointment_date")

        if selected_date < date.today():
            raise forms.ValidationError("You cannot select a past date.")
        
        if selected_date.weekday() == 6:
            raise forms.ValidationError("Appointments cannot be booked on Sundays.")
        
        blocked_dates = [
            date(2024, 12, 24),
            date(2024, 12, 25),
            date(2024, 12, 26),
            date(2024, 12, 31),
            date(2025, 1, 1),
            date(2025, 2, 3),
            date(2025, 3, 17),
            date(2025, 4, 21),
            date(2025, 5, 5),
            date(2025, 6, 2),
            date(2025, 8, 4),
            date(2025, 10, 27),
            date(2025, 12, 24),
            date(2025, 12, 25),
            date(2025, 12, 26),
            date(2025, 12, 31),
        ]
        if selected_date in blocked_dates:
            raise forms.ValidationError(f"Appointments cannot be booked on {selected_date}. Please pick another date.")

        return selected_date