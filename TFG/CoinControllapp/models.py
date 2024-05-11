from django.db import models
from django.contrib.auth.models import User

class Gasto(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    fechaFin =models.DateField(null=True,blank=True)
    categoria = models.CharField(max_length=100)
    notas = models.TextField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pagoUnico = models.BooleanField(default=False)
    frecuencia_choices = [
        ('mensual', 'Mensual'),
        ('semanal', 'Semanal'),
        ('anual', 'Anual'),
        # Agrega más opciones según sea necesario
    ]
    frecuencia = models.CharField(max_length=10, choices=frecuencia_choices, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Ingreso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    fechaFin = models.DateField(blank=True, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return f"Ingreso de {self.monto} ({self.categoria}) desde {self.fecha_inicio} hasta {self.fecha_fin if self.fecha_fin else 'presente'}"
