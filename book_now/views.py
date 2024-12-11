from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Appointment
from treatments.models import Treatment
from .forms import AppointmentForm


@login_required
def book_appointment(request):
    if request.method == 'POST':
        appointment_form = AppointmentForm(request.POST)
        if appointment_form.is_valid():
            appointment = appointment_form.save(commit=False)
            appointment.user = request.user

            # Check for existing appointments
            if Appointment.objects.filter(
                appointment_date=appointment.appointment_date,
                appointment_time=appointment.appointment_time
            ).exists():
                messages.error(request, "This time is fully booked. Please choose another time")
            else:
                appointment.save()
                messages.success(request, "Appointment booked successfully!")
                return redirect('list_appointments')  
        else:
            # Form is invalid; show errors in the template
            messages.error(request, "There was an error with your booking. Please try again.")

    else:
        # Initialize form for GET request
        appointment_form = AppointmentForm()

    # Render form for both invalid POST and GET requests
    return render(request, 'book_now.html', {'appointment_form': appointment_form})


def list_appointments(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'list_appointments.html', {'appointments': appointments})


@login_required
def list_appointments(request):
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        if booking_id:
            appointment = get_object_or_404(Appointment, booking_id=booking_id, user=request.user)
            appointment.delete()
            messages.success(request, "Appointment cancelled successfully!")

    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'list_appointments.html', {'appointments': appointments})