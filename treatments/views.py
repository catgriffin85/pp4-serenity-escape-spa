from django.shortcuts import render
from django.views import generic
from django.templatetags.static import static
from .models import Treatment


# Create your views here.
class TreatmentList(generic.ListView):
    """
    Renders a paginated list of active treatments, grouped by category.
    Displays instance of :model: `treatments.Treatment`.
    **Context**
    ``treatments``
        The most recent instance of :model:`treatments.Treatment`.
    **Template**
    :template:`treatments/treatments_page.html
    """
    queryset = Treatment.objects.all().filter(status=1).order_by("category")
    template_name = "treatments_page.html"
    paginate_by = 6
    context_object_name = "treatments"
