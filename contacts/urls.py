from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ContactsView.as_view(), name='contacts.list'),
]