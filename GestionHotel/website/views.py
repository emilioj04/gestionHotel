from django.shortcuts import render
from Reservas.views import *

# Create your views here.

def home(request):
    return render(request, 'index.html')

def testimonios(request):
    return render(request, 'testimonios.html')

def contacto(request):
    return render(request, 'contacto.html')

def pago(request):
    return render(request, 'pago.html')

def habitacion(request, id):
    return render(request, 'habitacion.html')