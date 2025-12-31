from django.contrib import admin
from .models import Cliente

# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "telefono",
        "email",
        "direccion",
        "fecha_creacion"
    )
    search_fields = ("nombre", "telefono", "email", "direccion")
    list_filter = ("fecha_creacion",)