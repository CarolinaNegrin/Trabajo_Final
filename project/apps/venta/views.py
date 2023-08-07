# Create your views here.
from django.shortcuts import render, redirect
from .forms import VentaForm
from .models import Venta
from django.http import HttpRequest, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import ListView

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
