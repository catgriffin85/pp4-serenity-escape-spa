from . import views
from django.urls import path

urlpatterns = [
    path("book-app/", views.BookApp.as_view(), name = "book-app"),
]