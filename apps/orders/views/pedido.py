from rest_framework.viewsets import ModelViewSet
from orders.models import Pedido
from orders.serializers.pedido import PedidoSerializer

class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.prefetch_related("detalles")
    serializer_class = PedidoSerializer