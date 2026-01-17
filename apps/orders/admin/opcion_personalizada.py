from django.contrib import admin
from orders.models.opcion_personalizada import OpcionPersonalizadaPedido

@admin.register(OpcionPersonalizadaPedido)
class OpcionPersonalizadaPedidoAdmin (admin.ModelAdmin):
    list_display = ("id", "detalle_personalizacion", "variante")
    list_filter = ("variante_tipo")
    search_fields = ("variante_nombre")