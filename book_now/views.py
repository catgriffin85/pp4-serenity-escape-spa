from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
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
                return redirect('list_appointments.html')  
        else:
            # Form is invalid; show errors in the template
            messages.error(request, "There was an error with your booking. Please try again.")

    else:
        # Initialize form for GET request
        appointment_form = AppointmentForm()

    # Render form for both invalid POST and GET requests
    return render(request, 'book_now.html', {'appointment_form': appointment_form})



@login_required
def list_appointments(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'book_now/list_appointments.html', {'appointment': appointment})