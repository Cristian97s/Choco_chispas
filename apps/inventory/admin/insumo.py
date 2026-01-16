from django.contrib import admin
from inventory.models import Insumo

@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
        "unidad_medida",
        "stock_actual",
        "stock_minimo"
    )
    list_filter = ("nombre",)