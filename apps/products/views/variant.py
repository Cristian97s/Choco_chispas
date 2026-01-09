from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from products.models import VarianteProducto
from products.serializers.variant import VarianteProductoSerializer

class VarianteProductoViewSet(ModelViewSet):
    queryset = VarianteProducto.objects.all()
    serializer_class = VarianteProductoSerializer
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_fields = ["tipo", "activo"]
    search_filter = ["nombre"]
    ordering_filter = ["precio_adicional"]
    ordering = ["tipo", "nombre"]