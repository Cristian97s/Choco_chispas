from rest_framework.viewsets import ModelViewSet
from inventory.models import ItemProduccion
from inventory.serializers.item_Produccion import ItemProduccionSerializer

class ItemProduccionViewSet(ModelViewSet):
    queryset = ItemProduccion.objects.all()
    serializer_class = ItemProduccionSerializer