from django.contrib.auth import get_user_model
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

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
