from django.contrib import admin
from orders.models import PedidoPersonalizado

@admin.register(PedidoPersonalizado)
class PedidoPersonalizadoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "detalle_pedido",
    )