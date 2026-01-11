from django.db import models
from users.models import Usuario
from clients.models import Cliente

class Pedido(models.Model):
    ESTADO_CHOICES = (
        ("PENDIENTE", "Pendiente"),
        ("EN_PROCESO", "En proceso"),
        ("ENTREGADO", "Entregado"),
        ("CANCELADO", "Cancelado"),
    )
    cliente = models.ForeignKey(
        Cliente,
        on_delete= models.SET_NULL,
        null=True,
        related_name="pedidos"
    )
    vendedor = models.ForeignKey(
        Usuario,
        on_delete= models.PROTECT,
        related_name= "ventas"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateField()
    observaciones = models.TextField(blank=True)
    estado_pedido = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default="PENDIENTE"
    )
    total_neto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        ordering = ["-fecha_creacion"]
    
    def __str__(self):
        return f"Pedido #{self.id}"