from . import views
from django.urls import path
from .views import homepage_view
from book_now.models import Review
from book_now.views import customer_review

urlpatterns = [
    path('', views.homepage_view, name='home'),
]