from . import views
from django.urls import path

urlpatterns = [
    path("book_now/", views.BookApp.as_view(), name = "book-app"),
]