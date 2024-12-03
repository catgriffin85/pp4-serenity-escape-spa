from django.db import models
from django.contrib.auth.models import User
from treatments.models import Treatment

# Create your models here.
class Appointment(models.Model):
    booking_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointments")
    treatment_selected = models.ForeignKey(Treatment, on_delete=models.CASCADE, related_name="appointments")
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    requests = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["appointment_date"]

    def __str__(self):
        return f"{self.booking_id} : {self.treatment}. {self.appointment_time}, {self.appointment_date}"
