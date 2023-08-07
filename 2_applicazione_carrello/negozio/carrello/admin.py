from django.contrib import admin

from .models import Cart, Product, CartItem


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "description", "price")


admin.site.register(Product, ProductAdmin)


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]
    list_display = ("id", "user", "numero_prodotti", "totale_carrello")

    def numero_prodotti(self, obj):
        return obj.products.count()

    def totale_carrello(self, obj):
        return sum([
            item.product.price * item.quantity
            for item in obj.cartitem_set.all()
        ])
