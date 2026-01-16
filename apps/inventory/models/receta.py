from django.db import models
from products.models import Producto

class Receta(models.Model):
    producto = models.OneToOneField(
        Producto,
        on_delete=models.CASCADE,
        related_name="receta"
    )
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"Receta de {self.producto.nombre}"