from . import views
from django.urls import path

urlpatterns = [
    path("treatments/", views.TreatmentList.as_view(), name = "treatments"),
]