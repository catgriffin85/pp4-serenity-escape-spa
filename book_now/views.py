from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
from django.templatetags.static import static
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from datetime import date
from .models import Appointment, Review
from .forms import AppointmentForm, ReviewForm
from treatments.models import Treatment


@login_required
def book_appointment(request):
    """
    Allows a logged-in user to book an appointment.
    Displays instance of :model: `book_now.Appointment`.
    Displays instance of :form: `book_now.AppointmentForm`.
    **Context**
    ``book_now``
        The most recent instance of :model: `book_now.Appointment`.
        The most recent instance of :form: `book_now.AppointmentForm`.
    **Template**
    :template:`book_now/book_now.html
    """
    appointment_form = AppointmentForm(request.POST or None)

    if request.method == 'POST':
        if appointment_form.is_valid():
            appointment = appointment_form.save(commit=False)
            appointment.user = request.user

            # Check for existing appointments
            if Appointment.objects.filter(
                appointment_date=appointment.appointment_date,
                appointment_time=appointment.appointment_time
            ).exists():
                messages.error(
                                request,
                                "This time is fully booked.Please try again")
            else:
                appointment.save()
                messages.success(request, "Appointment booked successfully!")
                return redirect('list_appointments')

    else:
        # Initialize form for GET request
        appointment_form = AppointmentForm()

    return render(request, 'book_now.html', {
        'appointment_form': appointment_form,
    })


def list_appointments(request):
    """
    Displays a list of appointments for the logged-in user.
    Displays instance of :model: `book_now.Appointment`.
    **Context**
    ``book_now``
        The most recent instance of :model: `book_now.Appointment`.
    **Template**
    :template:`book_now/list_appointment.html
    """
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'list_appointments.html',
                  {'appointments': appointments})


@login_required
def edit_appointment(request, booking_id):
    """
    Allows a logged-in user to edit an existing appointment.
    Displays instance of :model: `book_now.Appointment`.
    Displays instance of :form: `book_now.AppointmentForm`.
    **Context**
    ``book_now``
        The most recent instance of :model: `book_now.Appointment`.
        The most recent instance of :form: `book_now.AppointmentForm`.
    **Template**
    :template:`book_now/edit_appointment.html
    """
    # Ensure the appointment belongs to the current user
    appointment = get_object_or_404(
        Appointment, booking_id=booking_id, user=request.user)

    if request.method == "POST":
        # Bind the request POST data to the existing appointment instance
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():

            if Appointment.objects.filter(
                appointment_date=appointment.appointment_date,
                appointment_time=appointment.appointment_time
            ).exists():
                messages.error(
                                request,
                                "This time is fully booked.Please try again")
            else:
                form.save()
                messages.success(
                                  request,
                                  "Your appointment has been updated!")
            return redirect('list_appointments')

        else:
            messages.error(
                           request,
                           "There was an error. Please try again.")
    else:
        # Populate the form with the existing appointment data
        form = AppointmentForm(instance=appointment)

    return render(request, 'edit_appointment.html', {'form': form,
                  'appointment': appointment})


@login_required
def list_appointments(request):
    """
    Displays a list of appointments for the logged-in user and handles
    appointment cancellations.
    Displays instance of :model: `book_now.Appointment`.
    **Context**
    ``book_now``
        The most recent instance of :model: `book_now.Appointment`.
    **Template**
    :template:`book_now/list_appointments.html
    """
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        if booking_id:
            appointment = get_object_or_404(Appointment,
                                            booking_id=booking_id,
                                            user=request.user)
            appointment.delete()
            messages.success(request, "Appointment cancelled successfully!")

    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'list_appointments.html',
                  {'appointments': appointments})


@login_required
def customer_review(request):
    """
    Allows a logged-in user to submit a review.
    Displays instance of :form: `book_now.ReviewForm`.
    **Context**
    ``book_now``
        The most recent instance of :form: `book_now.ReviewForm`..
    **Template**
    :template:`book_now/review.html
    """

    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, "Thank you for your review.")
            review_form = ReviewForm()

        else:
            messages.error(
                           request,
                           "There was an error. Please try again.")

    else:
        review_form = ReviewForm()

    return render(request, 'review.html', {'review_form': review_form})
