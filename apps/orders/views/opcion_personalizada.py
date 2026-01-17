from rest_framework.viewsets import ModelViewSet
from orders.models import OpcionPersonalizadaPedido
from orders.serializers.opcion_personalizada import (
    OpcionPersonalizadaPedidoSerializer
)

class OpcionPersonalizadaPedidoViewSet(ModelViewSet):
    queryset = OpcionPersonalizadaPedido.objects.select_related(
        "detalle_personalizacion", "variante"
    )
    serializer_class = OpcionPersonalizadaPedidoSerializer