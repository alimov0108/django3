from django.db import models


class Kostyum(models.Model):
    narxi = models.IntegerField(default=24)
    sifati = models.CharField(max_length=24)
    davlati = models.CharField(max_length=24)
# Create your models here.
