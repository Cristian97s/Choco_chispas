from django.db import models
from products.models import Producto

class Receta(models.Model):
    producto = models.OneToOneField(
        Producto,
        on_delete=models.CASCADE,
        related_name="receta"
    )
    descripcion = models.TextField(blank=True)

    class Meta:
        db_table = 'receta'
        verbose_name = 'receta'
        verbose_name_plural = 'recetas'

    def __str__(self):
        return f"Receta de {self.producto.nombre}"
