# URLs
from rest_framework.routers import DefaultRouter
from api.views import ProductViewSet, DiscountViewSet, OrderViewSet

router = DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"discounts", DiscountViewSet)
router.register(r"orders", OrderViewSet)
