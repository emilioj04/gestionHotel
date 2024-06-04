# Generated by Django 5.0.6 on 2024-06-04 01:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Huespedes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarjeta',
            name='huesped',
        ),
        migrations.AddField(
            model_name='huesped',
            name='tarjeta',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='huesped', to='Huespedes.tarjeta'),
        ),
        migrations.AlterField(
            model_name='huesped',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='cvv',
            field=models.CharField(max_length=4),
        ),
    ]