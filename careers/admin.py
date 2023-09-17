from django.contrib import admin
from . import models

class CareersAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(models.Career, CareersAdmin)