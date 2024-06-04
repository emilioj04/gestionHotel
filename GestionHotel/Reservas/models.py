from django.db import models
from Empleados.models import Empleado
from Huespedes.models import Huesped


class TipoHabitacion(models.TextChoices):
    SENCILLA = 'S', 'Sencilla'
    DOBLE = 'D', 'Doble'
    TRIPLE = 'T', 'Triple'
    MATRIMONIAL = 'M', 'Matrimonial'
    PRESIDENCIAL = 'P', 'Presidencial'
    VIP = 'V', 'VIP'
    FAMILIAR = 'F', 'Familiar'


class Habitacion(models.Model):
    numero = models.IntegerField()
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
    empleado_list = models.ForeignKey(Empleado, related_name='servicios', on_delete=models.DO_NOTHING,default=None)

    def __str__(self):
        return self.tipoServicio


class EstadoReserva(models.TextChoices):
    RESERVADA = 'RESERVADA', 'RESERVADA'
    CANCELADA = 'CANCELADA', 'CANCELADA'
    LIBERADA = 'LIBERADA', 'LIBERADA'


class Reserva(models.Model):
    fechaEntrada = models.DateField()
    fechaSalida = models.DateField()
    estado = models.CharField(max_length=10, choices=EstadoReserva.choices, default=EstadoReserva.RESERVADA)
    nroHabitaciones = models.IntegerField()
    huesped = models.ForeignKey(Huesped, on_delete=models.DO_NOTHING, related_name='reservas')
    habitacionList = models.ForeignKey(Habitacion, on_delete=models.DO_NOTHING, related_name='reservas',default=None)
    servicioList = models.ForeignKey(Servicio, related_name='reservas',default=None, on_delete=models.DO_NOTHING)

    def calcular_costo_total(self):
        return sum(habitacion.costo for habitacion in self.habitacionList.all())

    def __str__(self):
        return str(self.id)
