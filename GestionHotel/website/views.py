from django.shortcuts import render
from Reservas.models import *

# Create your views here.

def home(request):
    return render(request, 'index.html')


def habitaciones(request):
    habitaciones = Habitacion.objects.all()
    content = {
        'habitaciones': habitaciones
        }
    return render(request, 'habitaciones.html', content)

def servicios(request):
    return render(request, 'servicios.html')

def testimonios(request):
    return render(request, 'testimonios.html')

def contacto(request):
    return render(request, 'contacto.html')

def pago(request):
    return render(request, 'pago.html')