# Create your views here.
from django.shortcuts import render, redirect
from .forms import VentaForm, TipoServicioForm, ServicioForm
from .models import Venta, Servicio, TipoServicio
from django.http import HttpRequest, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy

def home (request):
    return render (request, 'venta/index.html')

def registrar_pedido(request: HttpRequest) -> HttpResponse:
    # Desde esta función los usuarios pueden registrar sus pedidos
    if request.method == "POST":
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()            
            return render(request, "home/index.html", {"mensaje": "Pedido registrado, nos comunicaremos a la brevedad. Muchas Gracias!"})
    else:  
        form = VentaForm()
        
    return render(request, "venta/registrar_pedido.html", {"form": form})


class VentaList(ListView):
    # Desde esta función un usuario miembro del staff puede listar todos los pedidos recibidos
    model = Venta

class TipoServicioCreateView(CreateView):
     # Desde esta función un usuario miembro del staff puede crear tipos de servicio
    model = TipoServicio
    form_class = TipoServicioForm
    success_url = reverse_lazy("venta:servicios")

def servicios(request):
    # Desde esta función se podrá visualizar todos los servicios disponibles
    servicios_registro = TipoServicio.objects.all()
    contexto = {"servicios": servicios_registro}
    return render (request, 'venta/servicios.html', contexto)

class ServicioCreateView(CreateView):
    # Desde esta función un usuario puede solicitar un servicio
    model = Servicio
    form_class = ServicioForm
    success_url = reverse_lazy("venta:confirmar")

def confirmar (request):
    # Esta función avisa al usuario que se registró su pedido
    return render(request, "venta/confirmar.html")

class ServicioList(ListView):
    # Desde esta función un usuario miembro del staff puede listar los servicios solicitados
    model = Servicio
    def get_queryset(self):
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = Servicio.objects.filter(fecha_servicio__icontains=consulta)
        else:
            object_list = Servicio.objects.all()
        return object_list
    
class ServicioDetail(DetailView):
    # Desde esta función un usuario miembro del staff puede ver el detalle de un servicio solicitado
    model = Servicio