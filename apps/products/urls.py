from rest_framework.routers import DefaultRouter
from products.views.category import CategoriaViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet, basename="categoria")

urlpatterns = router.urls
