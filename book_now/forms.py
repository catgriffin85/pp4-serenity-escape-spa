from django import forms
from .models import BookAppointment
from treatments.models import Treatment

class AppointmentForm(forms.ModelForm):
    treatment = forms.ModelChoiceField(queryset=Treatments.objects.all(), required=True)
    date = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = BookAppointment
        fields = ['treament', 'date', 'time']