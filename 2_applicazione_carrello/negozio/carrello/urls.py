from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, CartItemViewSet

router = DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"cart-items", CartItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
