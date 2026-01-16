from django.db import models
from inventory.models.insumo import Insumo
from inventory.models.receta import Receta

class RecetaInsumo(models.Model):
    receta = models.ForeignKey(
        Receta,
        on_delete=models.CASCADE,
        related_name="insumos"
    )
    insumo = models.ForeignKey(
        Insumo,
        on_delete=models.PROTECT
    )
    cantidad_requerida = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ("receta","insumo")

    def __str__(self):
        return f"{self.insumo.nombre} - {self.cantidad_requerida}"