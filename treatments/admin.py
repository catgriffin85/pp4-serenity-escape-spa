from django.contrib import admin
from .models import Treatment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Treatment)
class TreatmentAdmin(SummernoteModelAdmin):

    list_display = ('category', 'treatment', 'status')
    search_fields = ['treatment']
    list_filter = ('category',)
    summernote_fields = ('content',)


# Register your models here.