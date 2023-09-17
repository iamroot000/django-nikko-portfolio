from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CareersView.as_view(), name='careers.list'),
]