from django.db import models
from orders.models import DetallePedido

class ItemProduccion(models.Model):
    ESTADO_CHOICES = (
        ("PENDIENTE_PRO", "Pendiente"),
        ("EN_PRODUCCION", "En produccion"),
        ("TERMINADO", "Terminado"),
    )
    
    detalle_pedido = models.ForeignKey(
        DetallePedido,
        on_delete=models.CASCADE,
        related_name="item_produccion"
    )
    fecha_produccion = models.DateField()
    prioridad = models.PositiveSmallIntegerField(default=1)
    comentarios_internos = models.TextField(blank=True)
    estado_produccion = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default="PENDIENTE_PRO"
    )

    def __str__(self):
        return f"Produccion #{self.id}"