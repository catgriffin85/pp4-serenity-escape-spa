from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def book_app(request):
    return HttpResponse("This is the book now page")