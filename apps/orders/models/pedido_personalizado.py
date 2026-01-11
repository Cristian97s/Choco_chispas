from django.db import models
from orders.models import DetallePedido

class PedidoPersonalizado(models.Model):
    detalle_pedido = models.OneToOneField(
        DetallePedido,
        on_delete= models.CASCADE,
        related_name="personalizacion"
    )
    description_personalizada = models.TextField(blank=True)
    imagen_referencia = models.ImageField(
        upload_to="personalizados/",
        null=True,
        blank=True
    )
    texto_personalizado = models.TextField(blank=True)

    def __str__(self):
        return f"Personalizacion #{self.id}"