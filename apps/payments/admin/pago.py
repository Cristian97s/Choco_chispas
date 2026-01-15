from django.contrib import admin
from payments.models import Pago

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "pedido",
        "metodo_pago",
        "monto",
        "estado_pago",
        "fecha_pago",
    )
    list_filter = ("estado_pago", "metodo_pago")
    search_fields = ("pedido__id",)