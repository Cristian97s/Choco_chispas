from rest_framework.routers import DefaultRouter
from inventory.views import (
    InsumoViewSet,
    RecetaViewSet,
    ItemProduccionViewSet,
)

router = DefaultRouter()
router.register(r"insumos", InsumoViewSet)
router.register(r"recetas", RecetaViewSet)
router.register(r"poduccion", ItemProduccionViewSet)

urlpatterns = router.urls