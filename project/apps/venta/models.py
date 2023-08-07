from django.db import models
from producto.models import Producto
from cliente.models import Cliente

# Create your models here.

class Venta (models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    producto_id = models.ForeignKey(Producto, on_delete=models.SET_NULL, blank=True, null=True)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True)
    cantidad = models.PositiveIntegerField(default=1, null=False, blank=False)
    def subtotal(self):
        subtotal = self.producto_id.precio * self.cantidad
        return subtotal

    def __str__(self):
        return f"{self.cliente_id} compró {self.cantidad} {self.producto_id}. Total ${self.subtotal()}"