from django.urls import path
from . import views
from .views import homepage_view

urlpatterns = [
    path('', views.homepage_view, name='home'),
]
