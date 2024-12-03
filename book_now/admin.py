from django.contrib import admin
from .models import Appointment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Appointment)
class AppointmentAdmin(SummernoteModelAdmin):

    list_display = ('name', 'user', 'treatment_selected')
    search_fields = ['name']
    list_filter = ('user',)
    summernote_fields = ('content',)

# Register your models here.
