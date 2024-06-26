# Generated by Django 5.0.6 on 2024-06-04 03:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empleados', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='dni',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='email',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='fechaNacimiento',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='genero',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='telefono',
        ),
        migrations.AddField(
            model_name='empleado',
            name='persona',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='empleado', to='core.persona'),
        ),
    ]
