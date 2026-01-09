from django.contrib import admin
from products.models import VarianteProducto

@admin.register(VarianteProducto)
class VarianteProductoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "tipo",
        "nombre",
        "precio_adicional",
        "activo",
    )
    list_filter = ("tipo", "nombre")
    search_fields = ("nombre",)
    list_editable = ("precio_adicional", "activo")