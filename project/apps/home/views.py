from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home/index.html")

def contacto(request):
    return render(request, "home/contacto.html")

