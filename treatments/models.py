from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Inactive"), (1, "Active"))

# Create your models here.
class Treatment(models.Model):
    category = models.CharField(max_length=200)
    treatment = models.CharField(max_length=200)
    treatment_id = models.IntegerField()
    description = models.TextField()
    duration = models.CharField(max_length=50)
    cost = models.CharField(max_length=50)
    status = models.IntegerField(choices=STATUS, default=0)