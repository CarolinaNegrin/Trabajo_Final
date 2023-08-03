from django.urls import path
from .views import home, register, login_request, datos_cliente
from django.contrib.auth.views import LogoutView
app_name = "cliente"

urlpatterns = [
    path("", home, name="home"),
    path('register/', register, name="register"),
    path('login/', login_request , name="login"),
    path('logout/', LogoutView.as_view(template_name="cliente/logout.html"), name="logout"),
    path('datos_cliente/', datos_cliente.as_view(template_name="cliente/datos_cliente.html"), name="datos_cliente"),
]
