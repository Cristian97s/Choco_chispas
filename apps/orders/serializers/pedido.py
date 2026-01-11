from rest_framework import serializers
from orders.models import Pedido
from orders.serializers.detalle_pedido import DetallePedidoSerializer

class PedidoSerializer(serializers.ModelSerializer):
    detalles = DetallePedidoSerializer(many = True)

    class Meta:
        model = Pedido
        fields = "__all__"
    
    def create(self, validated_data):
        detalles_data = validated_data.pop("detalles")
        pedido = Pedido.objects.create(**validated_data)

        total = 0
        for detalle in detalles_data:
            item = pedido.detalles.create(**detalle)
            total += item.subtotal()

        pedido.total_neto = total
        pedido.save()
        return pedido