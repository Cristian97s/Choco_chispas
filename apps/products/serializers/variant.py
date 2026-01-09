from rest_framework import serializers
from products.models import VarianteProducto

class VarianteProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VarianteProducto
        fields = (
            "id",
            "tipo",
            "nombre",
            "precio_adicional",
            "activo",
        )