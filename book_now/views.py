from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
from .models import Appointment, BookAppointment, TimeSlot
from treatments.models import Treatment
from .forms import AppointmentForm

# Create your views here.
class BookApp(generic.ListView):
    queryset = Appointment.objects.all().order_by("appointment_date")
    template_name = "book_now.html"
    context_object_name = "book_now"


@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user

            existing_appointments = BookAppointment.objects.filter(
                date = appointment.date, time = appointment.time 
            ).count()
            if existing_appointments >=2:
                messages.error(request, "This time is fully booked. Please try another time.")
            else:
                appointment.save()
                messages.success(request, "Appointment booked successfully!")
                return redirect('home')
        else:
            form = AppointmentForm()
        
        return render(request, 'book_now/book_now.html', {'form':form})


@login_required
def list_appointments(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'book_now/list_appointments.html', {'appointments': appointments})