from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from book_now.models import Review
from book_now.views import customer_review

# Create your views here.
def homepage_view(request):

    return render(
        request,"homepage/homepage.html"
        )

def homepage_view(request):
    reviews = Review.objects.filter(approved=True).order_by('-created_on')[:3]
    return render(request, 'homepage/homepage.html', {'reviews': reviews})
