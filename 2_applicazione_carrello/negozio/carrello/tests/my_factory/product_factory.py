import random

import factory

from carrello.models import Product, Categories


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: f"Prodotto {n}")
    description = factory.Sequence(lambda n: f"Descrizione prodotto {n}")
    category = random.choice([option.value for option in Categories])
    price = factory.Faker("pydecimal", left_digits=2, right_digits=2, positive=True)
