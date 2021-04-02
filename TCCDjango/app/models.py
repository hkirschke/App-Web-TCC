"""
Definition of models.
"""

from django.db import models

# Create your models here.


class ModelTileLine(models.Model):

    Name = models.CharField(max_length=100)
    Regiao = models.CharField(max_length=100)
    Mes = models.CharField(max_length=100)
    Casos = models.IntegerField()
    Recuperados = models.IntegerField()
    Mortos = models.IntegerField()