from django.urls import path
from . import views

app_name = "venta"

urlpatterns = [
    path("", views.home, name="home"),
    path("registrar/pedido/", views.registrar_pedido, name="registrar_pedido"),
    path("venta/list/", views.VentaList.as_view(), name="venta_list"),
    path("registrar/tiposervicio/", views.TipoServicioCreateView.as_view(), name="registrar_tiposervicio"),
    path("servicios", views.servicios, name="servicios"),
    path("registrar/servicio/", views.ServicioCreateView.as_view(), name="registrar_servicio"),
    path("confirmar", views.confirmar, name="confirmar"),
    path('servicio/list/', views.ServicioList.as_view(), name="servicio_list"),
    path("servicio/detail/<int:pk>", views.ServicioDetail.as_view(), name="servicio_detail"),
]
