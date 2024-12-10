from django.contrib import admin
from .models import Appointment
from django_summernote.admin import SummernoteModelAdmin
from datetime import time

@admin.register(Appointment)
class AppointmentAdmin(SummernoteModelAdmin):

    list_display = ('name', 'user', 'treatment_selected', 'appointment_date', 'appointment_time')
    search_fields = ['name']
    list_filter = ('appointment_date',)
    summernote_fields = ('content',)
