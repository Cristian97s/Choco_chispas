from rest_framework.routers import DefaultRouter
from products.views.category import CategoriaViewSet
from products.views.product import ProductoViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet, basename="categoria")
router.register(r"productos", ProductoViewSet, basename="producto")

urlpatterns = router.urls
