from django.contrib import admin
from products.models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
        "categoria",
        "precio",
        "stock",
        "activo",
    )
    list_filter = ("activos", "categoria")
    search_fields = ("nombre",)
    list_editable = ("precio", "stock", "activo")