from django import forms
from .models import Venta, Servicio, TipoServicio

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ["producto_id", "cliente_id", "cantidad"]

class TipoServicioForm(forms.ModelForm):
    class Meta:
        model = TipoServicio
        fields = "__all__"

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = "__all__"
        widget = forms.DateInput(attrs={'type': 'date'})