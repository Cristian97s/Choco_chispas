from rest_framework.viewsets import ModelViewSet
from inventory.models import Insumo
from inventory.serializers.insumo import InsumoSerializer

class InsumoViewSet(ModelViewSet):
    queryset = Insumo.objects.all()
    serializer_class = InsumoSerializer