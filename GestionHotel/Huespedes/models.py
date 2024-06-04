from django.db import models
from core.models import Persona


# Create your models here.

class TipoCliente(models.TextChoices):
    VIP = 'VIP', 'VIP'
    ESTANDAR = 'ESTANDAR', 'ESTANDAR'
    NUEVO = 'NUEVO', 'NUEVO'
    FRECUENTE = 'FRECUENTE', 'FRECUENTE'


class Huesped(Persona):
    idHuesped = models.AutoField(primary_key=True)
    tipoCliente = models.CharField(max_length=10, choices=TipoCliente.choices, default=TipoCliente.NUEVO)

    def __str__(self):
        return self.persona.nombre + ' ' + self.persona.apellido


class Tarjeta(models.Model):
    nroTarjeta = models.AutoField(primary_key=True)
    huesped = models.ForeignKey(Huesped, on_delete=models.CASCADE, related_name='tarjeta')
    fechaExpiracion = models.DateField()
    cvv = models.CharField(max_length=4)

    def __str__(self):
        return self.nroTarjeta
