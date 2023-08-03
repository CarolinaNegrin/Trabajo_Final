from django.urls import path
from .views import home, contacto
from cliente.views import login_request
from django.contrib.auth.views import LogoutView

app_name = "home"

urlpatterns = [
    path("", home, name="home"),
    path("contacto/", contacto, name="contacto"),
    
    
]
