from django import forms
from django.contrib.auth.decorators import login_required
from .models import Appointment, TIMESLOT_CHOICES, Review
from datetime import date
from treatments.models import Treatment


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
        labels = {
            "name": "Your Name:",
            "treatment_selected": "Select a treatment:",
            "appointment_date": "Choose your preferred date:",
            "appointment_time": "Choose your preferred time:",
            "requests": "Please outline any special requests or any information we should be aware of:",
        }
    
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


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["name", "treatment_review", "score", "review"]
        labels = {
            "name": "Your name:",
            "treatment_review": "Select a treatment:",
            "score": "How would you score our service out of 5?",
            "review": "Please leave your review:",
        }