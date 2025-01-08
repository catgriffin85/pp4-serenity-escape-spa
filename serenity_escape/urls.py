"""
URL configuration for serenity_escape project.
"""
from django.contrib import admin
from django.urls import path, include
from homepage import views as homepage_view


urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include("homepage.urls"), name="homepage-urls"),
    path('', include("treatments.urls"), name="treatments"),
    path('', include("book_now.urls"), name="book_now"),
    path('', include("book_now.urls"), name="list_appointment"),
    path('', include("book_now.urls"), name="review"),
]
