from django.db import models
from core.models import Persona


# Create your models here.
class TipoEmpleado(models.TextChoices):
    MASAJISTA = 'MASAJISTA', 'MASAJISTA'
    RECEPCIONISTA = 'RECEPCIONISTA', 'RECEPCIONISTA'
    LIMPIEZA = 'LIMPIEZA', 'LIMPIEZA'
    COCINA = 'COCINA', 'COCINA'
    SEGURIDAD = 'SEGURIDAD', 'SEGURIDAD'
    MANTENIMIENTO = 'MANTENIMIENTO', 'MANTENIMIENTO'
    VALET = 'VALET', 'VALET'
    CAMARERO = 'CAMARERO', 'CAMARERO'


class Empleado(Persona):
    idEmpleado = models.AutoField(primary_key=True)
    tipoEmpleado = models.CharField(max_length=15, choices=TipoEmpleado.choices, default=TipoEmpleado.MASAJISTA)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def __str__(self):
        return self.persona.nombre + ' ' + self.persona.apellido
