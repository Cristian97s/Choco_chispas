from django.contrib import admin
from inventory.models import ItemProduccion

@admin.register(ItemProduccion)
class ItemProduccionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "detalle_pedido",
        "fecha_produccion",
        "prioridad",
        "comentarios_internos",
        "estado_produccion",
    )
    list_filter = ("estado_produccion",)