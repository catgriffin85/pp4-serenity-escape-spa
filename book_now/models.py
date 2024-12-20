from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from treatments.models import Treatment
from datetime import time


# Create your models here.
TIMESLOT_CHOICES = [
    ("08:00", "08:00 AM"),
    ("09:00", "09:00 AM"),
    ("10:00", "10:00 AM"),
    ("11:00", "11:00 AM"),
    ("12:00", "12:00 PM"),
    ("13:00", "01:00 PM"),
    ("14:00", "02:00 PM"),
    ("15:00", "03:00 PM"),
    ("16:00", "04:00 PM"),
    ("17:00", "05:00 PM"),
    ("18:00", "06:00 PM"),
    ("19:00", "07:00 PM"),
    ("20:00", "08:00 PM"),
]


class Appointment(models.Model):
    booking_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer")
    treatment_selected = models.ForeignKey('treatments.Treatment', on_delete=models.CASCADE, related_name="appointments")
    appointment_date = models.DateField()
    appointment_time = models.CharField(max_length=5, choices=TIMESLOT_CHOICES)
    requests = models.CharField(max_length=200, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["appointment_date", "appointment_time"]

    def __str__(self):
        return f"{self.booking_id}/{self.name} - {self.treatment_selected} at {self.appointment_time} on {self.appointment_date}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewer")
    name = models.CharField(max_length=50)
    treatment_review = models.ForeignKey('treatments.Treatment', on_delete=models.CASCADE, related_name="treatment_review")
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return f"{self.score}/5 - {self.review}"

    