from django.contrib.auth import get_user_model
from django.test import TestCase

from carrello.models import Categories, Product, Cart
from .my_factory import ProductFactory
from ..services import Proxy


class TestProductManager(TestCase):
    def setUp(self) -> None:
        self.prodotto1 = ProductFactory(category=Categories.FOOD, price=10.00)
        self.prodotto2 = ProductFactory(category=Categories.FOOD, price=15.00)
        self.prodotto3 = ProductFactory(category=Categories.CLOTHES, price=17.00)

    def test_given_product_list_when_get_price_then_return_total_price_by_category(self):
        total_price = Product.objects.get_total_price(category=Categories.FOOD)
        self.assertEqual(total_price, 25.00)


class TestProxy(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(username='test', password='test')
        self.carrello = Cart.objects.create(user=self.user)
        self.product = ProductFactory(category=Categories.FOOD, price=10.00)

    def test_proxy_aggiungi_elemento_a_carrello(self):
        Proxy.aggiungi_elemento_a_carrello(pk=self.carrello.id, product_pk=self.product.id)
        self.assertEqual(Cart.objects.get(id=self.carrello.id).products.count(), 1)
