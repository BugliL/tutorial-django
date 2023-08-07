from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, CartItemViewSet, CartViewSet

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="products")
router.register(r"cart-items", CartItemViewSet, basename="cart-items")
router.register(r"carts", CartViewSet, basename="carts")

urlpatterns = [
    path("", include(router.urls)),
]
