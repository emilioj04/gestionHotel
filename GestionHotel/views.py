from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def habitaciones(request):
    return render(request, 'habitaciones.html')

def servicios(request):
    return render(request, 'servicios.html')

def testimonios(request):
    return render(request, 'testimonios.html')

def contacto(request):
    return render(request, 'contacto.html')

def pago(request):
    return render(request, 'pago.html')