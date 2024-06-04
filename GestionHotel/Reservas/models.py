from django.db import models
from Empleados.models import Empleado

class TipoHabitacion(models.TextChoices):
    SENCILLA = 'S', 'Sencilla'
    DOBLE = 'D', 'Doble'
    TRIPLE = 'T', 'Triple'
    MATRIMONIAL = 'M', 'Matrimonial'
    PRESIDENCIAL = 'P', 'Presidencial'
    VIP = 'V', 'VIP'
    FAMILIAR = 'F', 'Familiar'

class Habitacion(models.Model):
    numero = models.IntegerField(editable=False)
    tipoHabitacion = models.CharField(max_length=1, choices=TipoHabitacion.choices, default=TipoHabitacion.SENCILLA)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidad = models.BooleanField(default=True)
    capacidad = models.IntegerField()

    def __str__(self):
        return str(self.numero)


class TipoServicio(models.TextChoices):
    SPA = 'SPA', 'SPA'
    PISCINA = 'PISCINA', 'PISCINA'
    GIMNASIO = 'GIMNASIO', 'GIMNASIO'
    PARQUEO = 'PARQUEO', 'PARQUEO'
    ALIMENTACION = 'ALIMENTACION', 'ALIMENTACION'
    MASAJES = 'MASAJES', 'MASAJES'


class Servicio(models.Model):
    tipoServicio = models.CharField(max_length=15, choices=TipoServicio.choices, default=TipoServicio.SPA)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    empleado_list = models.ManyToManyField(Empleado, related_name='servicio_list')

    def __str__(self):
        return self.tipoServicio

