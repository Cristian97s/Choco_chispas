from django.db import models
from orders.models import Pedido

class Pago(models.Model):
    METODO_PAGO_CHOICES = (
        ("EFECTIVO", "Efectivo"),
        ("TRANSFERENCIA", "Transferencia"),
        ("TARJETA", "Tarjeta"),
    )

    ESTADO_PAGO_CHOICES = (
        ("PENDIENTE", "Pendiente"),
        ("CONFIRMADO", "Confirmado"),
        ("RECHAZADO", "Rechazado"),
    )

    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.PROTECT,
        related_name="pagos"
    )

    metodo_pago = models.CharField(max_length= 20, choices=METODO_PAGO_CHOICES)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    estado_pago = models.CharField(max_length=20, choices=ESTADO_PAGO_CHOICES, default="PENDIENTE")
    fecha_pago = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-fecha_pago"]

    def __str__(self):
        return f"Pago #{self.id} - Pedido {self.pedido.id}"