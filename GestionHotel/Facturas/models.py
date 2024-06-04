from django.db import models
from Reservas.models import Reserva,Servicio
# Create your models here.
PORCENTAJE_IMPUESTOS = 0.15


class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    reserva = models.ForeignKey(Reserva, on_delete=models.DO_NOTHING, related_name='facturas')
    servicioList = models.ManyToManyField(Servicio, related_name='facturas')
    totalServicios = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    totalHabitaciones = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    totalImpuestos = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)


    def calcular_total(self):
        self.totalServicios = sum(servicio.costo for servicio in self.servicioList.all())
        self.totalHabitaciones = self.reserva.calcular_costo_total()  # Calculamos el costo total de la reserva
        self.subtotal = self.totalServicios + self.totalHabitaciones
        self.totalImpuestos = self.subtotal * PORCENTAJE_IMPUESTOS
        self.total = self.subtotal + self.totalImpuestos
        self.save()

    def __str__(self):
        return str(self.id)