from django.db import models
from django.contrib.auth.models import User
from treatments.models import Treatment
from datetime import time

# Create your models here.
class Appointment(models.Model):
    booking_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer")
    treatment_selected = models.ForeignKey('treatments.Treatment', on_delete=models.CASCADE, related_name="appointments")
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    requests = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["appointment_date"]

    def __str__(self):
        return f"{self.booking_id}/{self.name} - {self.treatment_selected} at {self.appointment_time} on {self.appointment_date}"


class BookAppointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="client")
    treatment = models.ForeignKey('treatments.Treatment', on_delete=models.CASCADE, related_name="booking")
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('date', 'time', 'treatment')
    
    def __str__(self):
        return f"{self.treatment} on {self.date} at {self.time}"
