from django.contrib import admin
from .models import Appointment
from .models import TimeSlot
from django_summernote.admin import SummernoteModelAdmin
from datetime import time

@admin.register(Appointment)
class AppointmentAdmin(SummernoteModelAdmin):

    list_display = ('name', 'user', 'treatment_selected')
    search_fields = ['name']
    list_filter = ('user',)
    summernote_fields = ('content',)

for hour in range(8,20):
    TimeSlot.objects.get_or_create(start_time=time(hour, 0), end_time=time(hour + 1, 0))
