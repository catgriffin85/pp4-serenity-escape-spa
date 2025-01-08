from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Treatment


@admin.register(Treatment)
class TreatmentAdmin(SummernoteModelAdmin):

    list_display = ('category', 'treatment', 'status')
    search_fields = ['treatment']
    list_filter = ('category',)
    summernote_fields = ('content',)
