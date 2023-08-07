import random

import factory
from django.test import TestCase

from carrello.models import Categories, Product


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: f"Prodotto {n}")
    description = factory.Sequence(lambda n: f"Descrizione prodotto {n}")
    category = random.choice([option.value for option in Categories])
    price = factory.Faker("pydecimal", left_digits=2, right_digits=2, positive=True)


class TestProductManager(TestCase):
    def setUp(self) -> None:
        self.prodotto1 = ProductFactory(category=Categories.FOOD, price=10.00)
        self.prodotto2 = ProductFactory(category=Categories.FOOD, price=15.00)
        self.prodotto2 = ProductFactory(category=Categories.CLOTHES, price=15.00)

    def test_given_product_list_when_get_price_then_return_total_price_by_category(self):
        total_price = Product.objects.get_total_price(category=Categories.FOOD)
        self.assertEqual(total_price, 25.00)
