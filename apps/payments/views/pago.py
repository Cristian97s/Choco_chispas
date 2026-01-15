from rest_framework.viewsets import ModelViewSet
from payments.models import Pago
from payments.serializers import PagoSerializer

class PagoViewSet(ModelViewSet):
    queryset = Pago.objects.select_related("pedido")
    serializer_class = PagoSerializer