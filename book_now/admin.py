from django.contrib import admin
from .models import Appointment, Review
from django_summernote.admin import SummernoteModelAdmin
from datetime import time

@admin.register(Appointment)
class AppointmentAdmin(SummernoteModelAdmin):

    list_display = ('name', 'user', 'treatment_selected', 'appointment_date', 'appointment_time')
    search_fields = ['name']
    list_filter = ('appointment_date',)
    summernote_fields = ('requests')


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):

    list_display = ('user', 'name', 'treatment_review', 'score', 'review', 'created_on')
    search_fields = ['score','treatment_review']
    list_filter = ('score', 'treatment_review', 'user')
    summernote_fields = ('review')