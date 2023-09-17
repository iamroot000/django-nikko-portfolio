from django.contrib import admin
from . import models

class JobsAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(models.Job, JobsAdmin)