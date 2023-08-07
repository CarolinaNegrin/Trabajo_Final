from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Cliente, Ciudad


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = "__all__"


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control, text-align"}),
            "email": forms.EmailInput(attrs={"class": "form-control, text-align"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }