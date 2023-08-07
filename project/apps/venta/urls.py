from django.urls import path
from . import views

app_name = "venta"

urlpatterns = [
    path("", views.home, name="home"),
    path("registrar/pedido/", views.registrar_pedido, name="registrar_pedido"),
    path("venta/list/", views.VentaList.as_view(), name="venta_list"),
]
