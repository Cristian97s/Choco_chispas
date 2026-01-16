from django.contrib import admin
from inventory.models import Receta, RecetaInsumo

class RecetaInsumoInline(admin.TabularInline):
    model = RecetaInsumo
    extra = 1

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    inlines = [RecetaInsumoInline]