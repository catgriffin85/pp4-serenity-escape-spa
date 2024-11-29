from django.shortcuts import render
from django.views import generic
from .models import Treatment

# Create your views here.
class TreatmentList(generic.ListView):
    queryset = Treatment.objects.all().filter(status=1).order_by("category")
    template_name = "treatments_page.html"
    context_object_name = "treatments"