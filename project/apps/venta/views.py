# Create your views here.
from django.shortcuts import render, redirect
from .forms import VentaForm, formset_factory
from .models import Producto

def realizar_venta(request):
    VentaDetalleFormSet = formset_factory(VentaForm, extra=1)

    if request.method == 'POST':
        formset = VentaDetalleFormSet(request.POST, prefix='venta')

        if venta_form.is_valid() and formset.is_valid():
            venta = venta_form.save()
            for form in formset:
                detalle_venta = form.save(commit=False)
                detalle_venta.venta = venta
                producto = detalle_venta.producto
                detalle_venta.subtotal = producto.precio * detalle_venta.cantidad
                detalle_venta.save()
            # Aquí puedes redirigir a otra página o realizar alguna acción después de guardar la venta y sus detalles.
            return redirect('ruta_redireccion')

    else:
        venta_form = VentaForm()
        formset = VentaDetalleFormSet(prefix='venta')

    productos = Producto.objects.all()
    return render(request, 'registrar_venta.html', {'venta_form': venta_form, 'formset': formset, 'productos': productos})