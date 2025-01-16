from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Appointment, Review
from treatments.models import Treatment
from datetime import date


class AppointmentTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="password")
        self.treatment = Treatment.objects.create(name="Massage", price=50.0)
        self.appointment = Appointment.objects.create(
            user=self.user,
            name="Test Appointment",
            treatment_selected=self.treatment,
            appointment_date=date.today(),
            appointment_time="09:00",
        )

    def test_book_appointment(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse("book_appointment"), {
            "name": "New Appointment",
            "treatment_selected": self.treatment.id,
            "appointment_date": date.today(),
            "appointment_time": "10:00",
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Appointment.objects.filter(
            name="New Appointment").exists())

    def test_edit_appointment(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse(
            "edit_appointment", args=[self.appointment.booking_id]), {
            "name": "Updated Appointment",
            "treatment_selected": self.treatment.id,
            "appointment_date": date.today(),
            "appointment_time": "11:00",
        })
        self.assertEqual(response.status_code, 302)
        self.appointment.refresh_from_db()
        self.assertEqual(self.appointment.name, "Updated Appointment")
        self.assertEqual(self.appointment.appointment_time, "11:00")

    def test_list_appointments(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(reverse("list_appointments"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.appointment.name)

    def test_cancel_appointment(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse("list_appointments"), {
            "booking_id": self.appointment.booking_id
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Appointment.objects.filter(
            id=self.appointment.id).exists())


class ReviewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="password")
        self.treatment = Treatment.objects.create(name="Facial", price=70.0)

    def test_submit_review(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse("review"), {
            "name": "Great Treatment",
            "treatment_review": self.treatment.id,
            "score": 5,
            "review": "Absolutely loved it!",
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Review.objects.filter(name="Great Treatment").exists())
