from django.shortcuts import render
from django.views import generic
from .models import Treatment
from django.templatetags.static import static

# Create your views here.
class TreatmentList(generic.ListView):
    queryset = Treatment.objects.all().filter(status=1).order_by("category")
    template_name = "treatments_page.html"
    paginate_by = 6
    context_object_name = "treatments"
