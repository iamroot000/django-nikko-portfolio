from django.db import models

class Career(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=800)
    years = models.CharField(max_length=100)