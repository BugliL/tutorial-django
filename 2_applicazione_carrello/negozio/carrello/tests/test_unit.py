from django.test import TestCase

from carrello.models import Categories, Product
from my_factory import ProductFactory


class TestProductManager(TestCase):
    def setUp(self) -> None:
        self.prodotto1 = ProductFactory(category=Categories.FOOD, price=10.00)
        self.prodotto2 = ProductFactory(category=Categories.FOOD, price=15.00)
        self.prodotto2 = ProductFactory(category=Categories.CLOTHES, price=15.00)

    def test_given_product_list_when_get_price_then_return_total_price_by_category(self):
        total_price = Product.objects.get_total_price(category=Categories.FOOD)
        self.assertEqual(total_price, 25.00)
