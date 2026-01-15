from rest_framework.routers import DefaultRouter
from payments.views import PagoViewSet

router = DefaultRouter()
router.register(r"pagos", PagoViewSet, basename="pago")

urlpatterns = router.urls
