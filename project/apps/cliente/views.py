from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect, render
from .models import Cliente
from .forms import ClienteForm
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . import forms
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import UpdateView
# Create your views here.

def home(request):
    clientes_registros = Cliente.objects.all()
    contexto = {"clientes": clientes_registros}
    # return render(request, "index.html", {"clientes": clientes_registros})
    return render(request, "cliente/index.html", contexto)

# def registrar_cliente(request: HttpRequest) -> HttpResponse:

#     if request.method == "POST":
#         form = ClienteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("cliente:home")
#     else:  # request.method == "GET"
#         form = ClienteForm()
#     return render(request, "cliente/crear.html", {"form": form})


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "home/index.html", {"mensaje": "Usuario creado 😊"})
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "cliente/register.html", {"form": form})


def login_request(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, "home/index.html", {"mensaje": "Inició sesión correctamente"})
    else:
        form = forms.CustomAuthenticationForm()
    return render(request, "cliente/login.html", {"form": form})

class datos_cliente(UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy("cliente:detail")
