# Generated by Django 5.0.6 on 2024-06-04 02:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Huespedes', '0003_alter_huesped_tarjeta'),
        ('Reservas', '0002_remove_servicio_empleado_list_servicio_empleado_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaEntrada', models.DateField()),
                ('fechaSalida', models.DateField()),
                ('estado', models.CharField(choices=[('RESERVADA', 'RESERVADA'), ('CANCELADA', 'CANCELADA'), ('LIBERADA', 'LIBERADA')], default='RESERVADA', max_length=10)),
                ('nroHabitaciones', models.IntegerField()),
                ('habitacionList', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='reservas', to='Reservas.habitacion')),
                ('huesped', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reservas', to='Huespedes.huesped')),
                ('servicioList', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='reservas', to='Reservas.servicio')),
            ],
        ),
    ]