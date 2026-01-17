from django.db import models
from orders.models.pedido_personalizado import PedidoPersonalizado
from products.models.variant import VarianteProducto

class OpcionPersonalizadaPedido(models.Model):
    detalle_personalizacion = models.ForeignKey(
        PedidoPersonalizado,
        on_delete=models.CASCADE,
        related_name="opciones"
    )
    variante = models.ForeignKey(
        VarianteProducto,
        on_delete=models.PROTECT,
        related_name="opciones_pedido"
    )

    class Meta:
        db_table = "opcion_personalizada_pedido"
        unique_together = ("detalle_personalizacion", "variante")
        verbose_name = "Opcion personalizada del pedido"
        verbose_name_plural = "Opciones personalizadas del pedido"

    def __str__(self):
        return f"{self.variante.nombre} ({self.detalle_personalizacion_id})"