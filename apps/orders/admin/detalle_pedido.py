from django.contrib import admin
from orders.models import DetallePedido

@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display= (
        "id",
        "pedido",
        "nombre_item",
        "cantidad",
        "precio_unitario",
        "es_personalizado",
    )
    list_filter = ("es_personalizado",)