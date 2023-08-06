from django.db import models

# Create your models here.

class Categoria (models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nombre

class Producto (models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    categoria_id= models.ForeignKey(Categoria, null=False, blank=False, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=100, blank=True, null=True)
    precio = models.FloatField(blank=False, null=False)
    stock = models.IntegerField(blank=True, null=True)
    personalizable = models.BooleanField(blank=True, null=True)
    imagen = models.ImageField(upload_to='img_productos', blank=True, null=True)

    def __str__(self):
        return self.nombre