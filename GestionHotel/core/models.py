from django.db import models

# Create your models here.
class Genero(models.TextChoices):
    MASCULINO = 'M', 'Masculino'
    FEMENINO = 'F', 'Femenino'
    OTRO = 'O', 'Otro'


class Persona(models.Model):
    nombre = models.CharField(max_length=100, default=None)
    apellido = models.CharField(max_length=100, default=None)
    dni = models.CharField(max_length=100,default=None)
    genero = models.CharField(max_length=1, choices=Genero.choices, default=Genero.MASCULINO)
    fechaNacimiento = models.DateField(default=None)
    email = models.EmailField(default=None)
    telefono = models.CharField(max_length=10, default=None)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre + ' ' + self.apellido




