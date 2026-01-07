from django.db import models
from products.models.category import Categoria

class Producto(models.Model):
    categora = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="productos"
    )
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveBigIntegerField(default=True)
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(
        upload_to="productos/",
        null=True,
        blank=True
    )
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["-creado"]
        indexes = [
            models.Index(fields=["nombre"]),
            models.Index(fields=["activo"])
        ]
    
    def __str__(self):
        return self.nombre