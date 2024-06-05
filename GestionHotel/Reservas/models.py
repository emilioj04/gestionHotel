from django.db import models
from Empleados.models import Empleado
from Huespedes.models import Huesped


class TipoHabitacion(models.TextChoices):
    SENCILLA = 'Sencilla', 'Sencilla'
    DOBLE = 'Doble', 'Doble'
    TRIPLE = 'Triple', 'Triple'
    MATRIMONIAL = 'Matrimonial', 'Matrimonial'
    PRESIDENCIAL = 'Presidencial', 'Presidencial'
    VIP = 'VIP', 'VIP'
    FAMILIAR = 'Familiar', 'Familiar'


class Habitacion(models.Model):
    imagen = models.URLField(max_length=200, null=True,blank=True, default="https://th.bing.com/th/id/R.aa826c4a6e33b35a5da84f2a987412d0?rik=H%2bmTxTshNQRzeg&pid=ImgRaw&r=0")
    numero = models.IntegerField()
    tipoHabitacion = models.CharField(max_length=20, choices=TipoHabitacion.choices, default=TipoHabitacion.SENCILLA)
    descripcion = models.TextField(default="Habitacion sencilla")
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidad = models.BooleanField(default=True)
    capacidad = models.IntegerField()
    reserva = models.ForeignKey('Reserva', on_delete=models.DO_NOTHING, related_name='habitacionList',default=None)

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
    servicioList = models.ForeignKey(Servicio, related_name='reservas_servicio',default=None, on_delete=models.DO_NOTHING)
    habitaciones = models.ForeignKey(Habitacion, on_delete=models.DO_NOTHING, related_name='reservas_habitacion',default=None)


    def calcular_costo_total(self):
        return sum(habitacion.costo for habitacion in self.habitacionList.all())

    def __str__(self):
        return str(self.id)
