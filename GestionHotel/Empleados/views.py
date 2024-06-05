from django.shortcuts import render, redirect
from .forms import EmpleadoForm


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


def habitacion(request, id):
    return render(request, 'habitacion.html')


def addEmpleado(request):
    if request.method == 'GET':
        return render(request, 'add_empleado.html', {
            'form': EmpleadoForm
        })
    else:
        try:
            form = EmpleadoForm(request.POST)
            newEmpleado = form.save(commit=False)
            newEmpleado.save()
            print(form)
            return redirect('home')
        except ValueError:
            return render(request, 'add_empleado.html', {
                'form': EmpleadoForm,
                'error': 'Bad data passed in. Try again.'
            })
