from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from products.models import Producto
from products.serializers.product import ProductoSerializer

class ProductoViewSet(ModelViewSet):
    queryset = Producto.objects.select_related("categoria")
    serializer_class = ProductoSerializer
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_fields = ["categoria", "activo"]
    search_filter = ["nombre"]
    ordering_filter = ["precio", "creado"]
    ordering = ["-creado"]