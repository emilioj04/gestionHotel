# Generated by Django 5.0.6 on 2024-06-04 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Empleados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(editable=False)),
                ('tipoHabitacion', models.CharField(choices=[('S', 'Sencilla'), ('D', 'Doble'), ('T', 'Triple'), ('M', 'Matrimonial'), ('P', 'Presidencial'), ('V', 'VIP'), ('F', 'Familiar')], default='S', max_length=1)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('disponibilidad', models.BooleanField(default=True)),
                ('capacidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoServicio', models.CharField(choices=[('SPA', 'SPA'), ('PISCINA', 'PISCINA'), ('GIMNASIO', 'GIMNASIO'), ('PARQUEO', 'PARQUEO'), ('ALIMENTACION', 'ALIMENTACION'), ('MASAJES', 'MASAJES')], default='SPA', max_length=15)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('empleado_list', models.ManyToManyField(related_name='servicio_list', to='Empleados.empleado')),
            ],
        ),
    ]
