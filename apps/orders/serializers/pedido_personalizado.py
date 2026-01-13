from rest_framework import serializers
from orders.models import PedidoPersonalizado

class PedidoPersonalizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoPersonalizado
        fields = "__all__"