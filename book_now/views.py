from django.shortcuts import render
from django.views import generic
from .models import Appointment

# Create your views here.
class BookApp(generic.ListView):
    queryset = Appointment.objects.all().order_by("appointment_date")
    template_name = "book_now.html"
    context_object_name = "book_now"