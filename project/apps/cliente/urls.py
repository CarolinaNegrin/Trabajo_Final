from django.urls import path
from .views import home, register, login_request, registrar_cliente, CiudadCreate
from django.contrib.auth.views import LogoutView
app_name = "cliente"

urlpatterns = [
    path("", home, name="home"),
    path('register/', register, name="register"),
    path('crear/cliente/', registrar_cliente, name="crear_cliente"),
    path('login/', login_request , name="login"),
    path('logout/', LogoutView.as_view(template_name="cliente/logout.html"), name="logout"),
    path('registrar/ciudad', CiudadCreate.as_view(), name="registrar_ciudad"),
]
