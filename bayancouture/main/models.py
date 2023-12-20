from django.db import models

# Create your models here.

class Abaya(models.Model):
    task = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
