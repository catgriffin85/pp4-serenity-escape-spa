from django.urls import path
from . import views

urlpatterns = [
    path("treatments/", views.TreatmentList.as_view(), name="treatments"),
]
