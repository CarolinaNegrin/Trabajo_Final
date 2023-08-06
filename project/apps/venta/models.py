from django.db import models
from producto.models import Producto
from cliente.models import Cliente

# Create your models here.

class Venta (models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True)
    cantidad = models.PositiveIntegerField(default=1, null=False, blank=False)
    def subtotal (self):
        subtotal = self.cantidad*self.producto.precio
        return subtotal
    