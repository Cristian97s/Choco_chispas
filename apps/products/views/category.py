from rest_framework.viewsets import ModelViewSet
from products.models import Categoria
from products.serializers.category import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
