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
    tarjeta = models.OneToOneField('Tarjeta', on_delete=models.DO_NOTHING, related_name='huesped',null=True, default=None)

    def __str__(self):
        return self.nombre + ' ' + self.apellido


class Tarjeta(models.Model):
    nroTarjeta = models.AutoField(primary_key=True)
    fechaExpiracion = models.DateField()
    cvv = models.CharField(max_length=4)

    def __str__(self):
        return str(self.nroTarjeta)
