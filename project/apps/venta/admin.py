from django.contrib import admin
from .models import Venta, Servicio, TipoServicio

# Register your models here.

admin.site.register(Venta)
admin.site.register(Servicio)
admin.site.register(TipoServicio)