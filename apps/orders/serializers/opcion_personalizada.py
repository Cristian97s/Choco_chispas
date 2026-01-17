from rest_framework import serializers
from orders.models import OpcionPersonalizadaPedido

class OpcionPersonalizadaPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpcionPersonalizadaPedido
        fields = "__all__"