from django.views.generic import ListView
from django.views import View
from django.http import JsonResponse

from .models import Job


class JobsListView(ListView):
    model = Job
    context_object_name = "jobs"
    template_name = 'jobs/jobs_list.html'

class JobDetailModalView(View):
    def get(self, request, pk):
        try:
            job = Job.objects.get(pk=pk)
            data = {'title': job.title, 'description': job.summary}
            return JsonResponse(data)
        except Job.DoesNotExist:
            return JsonResponse({'error': 'Job not found'}, status=404)