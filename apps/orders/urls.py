from rest_framework.routers import DefaultRouter
from orders.views.pedido import PedidoViewSet
from orders.views.opcion_personalizada import OpcionPersonalizadaPedidoViewSet

router = DefaultRouter()
router.register(r"pedidos", PedidoViewSet, basename="pedido")
router.register(r"opciones-personalizadas", OpcionPersonalizadaPedidoViewSet, basename="opciones-personalizadas")

urlpatterns = router.urls