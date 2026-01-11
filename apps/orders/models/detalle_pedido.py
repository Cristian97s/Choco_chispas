from django.db import models
from products.models import Producto
from orders.models import Pedido

class DetallePedido(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete= models.CASCADE,
        related_name="detalles"
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.SET_NULL,
        null=True
    )
    nombre_item = models.CharField(max_length=150)
    cantidad = models.PositiveBigIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    es_personalizado = models.BooleanField(default=False)

    def subtotal(self):
        return self.cantidad * self.precio_unitario
    
    def __str__(self):
        return f"{self.nombre_item} ({self.cantidad})"