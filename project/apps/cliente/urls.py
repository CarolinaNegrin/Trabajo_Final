from django.urls import path
from .views import home
app_name = "cliente"

urlpatterns = [
    path("", home, name="home")
]
