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
    

class TipoServicio(models.Model):
    nombre = models.CharField(max_length=150, blank=False, null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    fecha = models.DateField(auto_now_add=True)
    tiposervicio_id = models.ForeignKey(TipoServicio, on_delete=models.SET_NULL, null=True, blank=True)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_servicio = models.DateField(blank=False, null=False)
    detalle = models.CharField(max_length=400, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    imagen = models.ImageField(upload_to='img_servicios', blank=True, null=True)

    def __str__(self):
        return f"Fecha de Solicitud {self.fecha.strftime('%Y-%m-%d')}, servicio {self.tiposervicio_id.nombre}, para el {self.fecha_servicio.strftime('%Y-%m-%d')}"

