from django.views.generic import ListView

from .models import Contact


class ContactsView(ListView):
    model = Contact
    context_object_name = "contacts"
    template_name = 'contacts/contacts_list.html'