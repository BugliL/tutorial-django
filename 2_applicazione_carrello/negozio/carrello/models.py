import enum
from _decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.functions import Coalesce


class Categories(enum.Enum):
    GENERIC = "GENERIC"
    FOOD = "FOOD"
    DRINKS = "DRINKS"
    CLOTHES = "CLOTHES"
    ELECTRONICS = "ELECTRONICS"


categories_choices = [(tag.value, tag.value) for tag in Categories]


class ProductManager2(models.Manager):
    def filter(self, *args, **kwargs):
        print('sono qui')
        return super().filter(*args, **kwargs).filter(price__gt=0)

class ProductManager(models.Manager):
    def get_total_price(self, category=None):
        # prima scrittura
        # return sum([product.price for product in self.filter(category=category)])

        # codice rifattorizzato
        somma_prezzo = Coalesce(models.Sum('price'), models.Value(Decimal(0.0)))
        return self.filter(category=category) \
            .aggregate(total_price=somma_prezzo) \
            .get('total_price')


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(
        max_length=100, choices=categories_choices, blank=False, null=False,
        default=Categories.GENERIC.value
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)

    objects = ProductManager()
    queryset2 = ProductManager2()

    class Meta:
        verbose_name = "Prodotto"
        verbose_name_plural = "Prodotti"

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="CartItem")

    class Meta:
        verbose_name = "Carrello"
        verbose_name_plural = "Carrelli"

    def __str__(self):
        return f"Carrello #{self.id} {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Elemento carrello"
        verbose_name_plural = "Elementi carrello"
