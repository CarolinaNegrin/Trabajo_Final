from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Ciudad(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre

class Cliente (models.Model):
    nombre = models.CharField(max_length=20, blank=False, null=False)
    apellido = models.CharField(max_length=20, blank=False, null=False)
    documento = models.IntegerField(max_length=8, blank=True, null=True)
    contacto = models.IntegerField(max_length=15, blank=True, null=True)
    domicilio = models.CharField(max_length=50, blank=True, null=True)
    nacimiento = models.DateField(null=True)
    ciudad_id = models.ForeignKey(Ciudad, blank=True, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"