# Generated by Django 5.0.4 on 2024-05-12 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoinControllapp', '0005_rename_fecha_inicio_ingreso_fecha_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingreso',
            name='nombre',
            field=models.CharField(default='No especificado', max_length=100),
        ),
    ]
