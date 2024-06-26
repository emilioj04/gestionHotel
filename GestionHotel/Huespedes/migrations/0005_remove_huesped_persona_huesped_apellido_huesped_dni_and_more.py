# Generated by Django 5.0.6 on 2024-06-04 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Huespedes', '0004_remove_huesped_apellido_remove_huesped_dni_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='huesped',
            name='persona',
        ),
        migrations.AddField(
            model_name='huesped',
            name='apellido',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='huesped',
            name='dni',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='huesped',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='huesped',
            name='fechaNacimiento',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='huesped',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='huesped',
            name='nombre',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='huesped',
            name='telefono',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
