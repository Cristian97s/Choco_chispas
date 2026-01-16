from rest_framework import serializers
from inventory.models import Receta, RecetaInsumo

class RecetaInsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecetaInsumo
        fields = ("insumo", "cantidad_requerida")

class RecetaSerializer(serializers.ModelSerializer):
    insumo = RecetaInsumoSerializer(many=True)

    class Meta:
        model = Receta
        fields = "__all__"

    def create(self, validated_data):
        insumos_data = validated_data.pop("insumos")
        receta = Receta.objects.create(**validated_data)

        for insumo in insumos_data:
            RecetaInsumo.objects.create(receta=receta, **insumo)

        return receta