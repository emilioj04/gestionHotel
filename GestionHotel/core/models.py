from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=100)
    genero = models.BooleanField(default=False)
    fechaNacimiento = models.DateField()
    email = models.EmailField()
    telefono = models.CharField(max_length=10)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre + ' ' + self.apellido

