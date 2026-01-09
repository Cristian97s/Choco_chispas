from django.db import models

class VarianteProducto(models.Model):
    TIPO_CHOICES = (
        ("TAMANO","Tamaño"),
        ("SABOR", "sabor"),
        ("DECORACION", "Decoración"),
        ("OTRO","otro")
    )

    tipo = models.CharField(
        max_length=30,
        choices= TIPO_CHOICES
    )
    nombre = models.CharField(max_length=100)
    precio_adicional = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "VarianteProdcuto"
        verbose_name_plural = "variantesproducto"
        unique_together = ("tipo", "nombre")
        ordering = ["tipo", "nombre"]

    def __str__(self):
        return f"{self.tipo} - {self.nombre}"
