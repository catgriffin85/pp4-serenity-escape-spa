from django.urls import path
from .views import book_appointment, list_appointments

urlpatterns = [
    path('book_appointment/', book_appointment, name='book_appointment'),
    path('list_appointments/', list_appointments, name='list_appointments'),
]
