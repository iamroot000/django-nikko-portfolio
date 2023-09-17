from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='media/images/')
    title = models.CharField(max_length=100, null=True)
    summary = models.CharField(max_length=200)
