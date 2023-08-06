from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home(request):
    return render(request, "home/base.html")

def contacto(request):
    return render(request, "home/contacto.html")



def contact_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']

        
            subject = f"Mensaje de contacto de {nombre}"
            body = f"Email del remitente: {email}\n\nMensaje:\n{mensaje}"
            sender_email = 'caro_negrin@hotmail.com' 

        
            send_mail(subject, body, sender_email, ['caro_negrin@hotmail.com'])  
            mensaje_enviado= f"{nombre}, su mensaje ha sido enviado correctamente. Nos pondemos en contaco a la brevedad. Muchas Gracias!"
          
            return render(request, 'home/index.html', {'mensaje': mensaje_enviado})

    else:
        form = ContactForm()

    return render(request, 'home/contacto.html', {'form': form})