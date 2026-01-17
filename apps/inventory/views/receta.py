from rest_framework.viewsets import ModelViewSet
from inventory.models import Receta
from inventory.serializers.receta import RecetaSerializer

class RecetaViewSet(ModelViewSet):
    queryset = Receta.objects.prefetch_related("insumos")
    serializer_class = RecetaSerializer