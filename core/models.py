from django.db import models


class Moshina(models.Model):
    nomi = models.CharField(max_length=23)
    turi = models.CharField(max_length=23)
    narxi = models.IntegerField(default=23)
# Create your models here.
