from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from carrello.models import Product, CartItem, Cart
from carrello.serializers import ProductSerializer, CartItemSerializer, CartSerializer

__all__ = [
    CartItemSerializer,
    CartSerializer,
    ProductSerializer,
]

from carrello.services import Proxy


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

    @action(detail=True, methods=["post"], url_path="aggiungi-prodotto/(?P<product_pk>[0-9]+)")
    def aggiungi_prodotto(self, request, *args, **kwargs):
        """
        Aggiunge un prodotto al carrello
        """
        carrello = Proxy.aggiungi_elemento_a_carrello(pk=kwargs.get("pk"), product_pk=kwargs.get("product_pk"))
        serializer = self.get_serializer_class()(carrello)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        return Cart.objects \
            .prefetch_related("cartitem_set__product") \
            .select_related("user") \
            .all()
