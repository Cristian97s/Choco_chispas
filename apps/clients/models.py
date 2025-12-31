from django.db import models

# Create your models here.
class Cliente (models.Model):
    nombre = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return f"{self.nombre} - {self.telefono}"