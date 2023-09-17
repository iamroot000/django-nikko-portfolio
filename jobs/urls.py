from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.JobsListView.as_view(), name='jobs.list'),
    path('job_detail_modal/<int:pk>/', views.JobDetailModalView.as_view(), name='jobs.detail'),
]