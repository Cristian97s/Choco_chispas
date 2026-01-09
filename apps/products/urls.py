from rest_framework.routers import DefaultRouter
from products.views.category import CategoriaViewSet
from products.views.product import ProductoViewSet
from products.views.variant import VarianteProductoViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet, basename="categoria")
router.register(r"productos", ProductoViewSet, basename="producto")
router.register(r"variantes", VarianteProductoViewSet, basename="variante")

urlpatterns = router.urls
