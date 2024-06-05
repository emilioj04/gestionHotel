# Generated by Django 5.0.6 on 2024-06-05 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservas', '0010_habitacion_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitacion',
            name='tipoHabitacion',
            field=models.CharField(choices=[('Sencilla', 'Sencilla'), ('Doble', 'Doble'), ('Triple', 'Triple'), ('Matrimonial', 'Matrimonial'), ('Presidencial', 'Presidencial'), ('VIP', 'VIP'), ('Familiar', 'Familiar')], default='Sencilla', max_length=20),
        ),
    ]
