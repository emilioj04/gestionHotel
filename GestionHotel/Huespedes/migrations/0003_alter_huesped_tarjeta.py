# Generated by Django 5.0.6 on 2024-06-04 02:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Huespedes', '0002_remove_tarjeta_huesped_huesped_tarjeta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='huesped',
            name='tarjeta',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='huesped', to='Huespedes.tarjeta'),
        ),
    ]
