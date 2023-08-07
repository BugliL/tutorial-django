from carrello.models import Product, CartItem
from carrello.serializers import ProductSerializer, CartItemSerializer, CartSerializer
from rest_framework import viewsets

__all__ = [
    CartItemSerializer,
    CartSerializer,
    ProductSerializer,
]


class ProductViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Product.objects.all()

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.all()


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer

    def get_queryset(self):
        return CartItem.objects.all().select_related('product')
