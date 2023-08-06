from django import forms
from .models import Venta

class VentaForm(forms.Form):
    class Meta:
        model = Venta
        fields = "__all__"
        