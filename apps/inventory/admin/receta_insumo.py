from django.contrib import admin
from inventory.models import RecetaInsumo

@admin.register(RecetaInsumo)
class RecetaInsumoAdmin(admin.ModelAdmin):
    list_display = (
        "receta",
        "insumo",
        "cantidad_requerida"
    )
    list_filter = ("cantidad_requerida",)