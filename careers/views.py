from django.views.generic import ListView

from .models import Career


class CareersView(ListView):
    model = Career
    context_object_name = "careers"
    template_name = 'careers/careers_list.html'