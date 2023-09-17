from django.contrib import admin
from . import models

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(models.Contact, ContactsAdmin)