from rest_framework import serializers
from orders.models import DetallePedido

class DetallePedidoSerializer(serializers.ModelSerializer):
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = DetallePedido
        fields = "__all__"

    def get_subtotal(self, obj):
        return obj.subtotal()