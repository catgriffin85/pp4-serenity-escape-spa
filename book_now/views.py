from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
from .models import Appointment, BookAppointment
from treatments.models import Treatment
from .forms import AppointmentForm

# Create your views here.
#class BookApp(generic.ListView):
#    queryset = Appointment.objects.all().order_by("appointment_date")
#    template_name = "book_now.html"
#    context_object_name = "book_now"


@login_required
def book_appointment(request):
    if request.method == 'POST':
        appointment_form = AppointmentForm(request.POST)
        if appointment_form.is_valid():
            appointment = appointment_form.save(commit=False)
            appointment.user = request.user

            # Check for existing appointments
            existing_appointments = appointment_form.Meta.model.objects.filter(
                date=appointment.date, time=appointment.time
            ).count()
            if existing_appointments >= 2:
                messages.error(request, "This time is fully booked. Please try another time.")
            else:
                appointment.save()
                messages.success(request, "Appointment booked successfully!")
                return redirect('list_appointments')  
        else:
            # Form is invalid; show errors in the template
            print("Form errors:", appointment_form.errors)

    else:
        # Initialize form for GET request
        appointment_form = AppointmentForm()

    # Render form for both invalid POST and GET requests
    return render(request, 'book_now.html', {'appointment_form': appointment_form})



@login_required
def list_appointments(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'book_now/list_appointments.html', {'appointment': appointment})