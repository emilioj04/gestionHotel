from django.contrib import admin
from .models import Habitacion, Servicio, Reserva
# Register your models here.
admin.site.register(Habitacion)
admin.site.register(Servicio)
admin.site.register(Reserva)