from django.contrib import admin
from orders.models import Pedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "cliente",
        "vendedor",
        "estado_pedido",
        "fecha_entrega",
        "total_neto",
        "total_pagado",
    )
    list_filter = ("estado_pedido", "fecha_creacion")
    search_fields = ("id",)