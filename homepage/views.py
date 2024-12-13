from django.shortcuts import render
from django.views import generic
from book_now.models import Review
from book_now.views import customer_review

# Create your views here.
def homepage_view(request):

    return render(
        request,"homepage/homepage.html"
        )

#def customer_review(request):
#    reviews = Review.objects.all().order_by('created_on')
#    paginator = Paginator(reviews, 1)
#    return render(request, 'homepage.html', {'reviews': reviews})

class ReviewList(generic.ListView):
    queryset = Review.objects.all().order_by("created_on")
    template_name = "review.html"
    paginate_by = 1
    context_object_name = "reviews"