# Generated by Django 5.0.4 on 2024-05-04 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoinControllapp', '0002_alter_gasto_fechafin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gasto',
            name='metodo_pago',
        ),
    ]
