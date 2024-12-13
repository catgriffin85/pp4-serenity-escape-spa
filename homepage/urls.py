from . import views
from django.urls import path
from .views import homepage_view

urlpatterns = [
    path('', views.homepage_view, name='home'),
]