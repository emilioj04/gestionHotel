from django.shortcuts import render
from .models import Habitacion, Servicio

# Create your views here.
def habitaciones(request):
    habitaciones = Habitacion.objects.all()
    content = {
        'habitaciones': habitaciones
        }
    return render(request, 'habitaciones.html', content)

def habitaciondetail(request, numero) :
    habitacion = Habitacion.objects.get(numero=numero)
    content = {
        'habitacion': habitacion
    }
    return render(request, 'habitaciondetail.html', content)

def servicios(request):
    servicios = Servicio.objects.all()
    content = {
        'servicios': servicios
    }
    return render(request, 'servicios.html', content)