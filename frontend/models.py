from django.db import models


class Noutbuk(models.Model):
    narxi = models.IntegerField(default=30)
    davlati = models.CharField(max_length=30)
    ishlasi = models.CharField(max_length=30)
# Create your models here.
