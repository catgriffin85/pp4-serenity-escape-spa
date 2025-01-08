from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from book_now.models import Review
from book_now.views import customer_review


# Create your views here.
def homepage_view(request):
    """
    Renders the Homepage
    Displays instance of :model: `book_now.Review`.
    **Context**
    ``book_now``
        The most recent instance of :model: `book_now.Review`.
    **Template**
    :template:`homepage/homepage.html
    """
    return render(
        request, "homepage/homepage.html"
        )


def homepage_view(request):

    reviews = Review.objects.filter(approved=True).order_by('-created_on')[:3]
    return render(request, 'homepage/homepage.html', {'reviews': reviews})
