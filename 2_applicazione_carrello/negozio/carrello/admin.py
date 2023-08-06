from django.contrib import admin

from .models import Cart, Product, CartItem


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price")


admin.site.register(Product, ProductAdmin)


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user",)
    inlines = [CartItemInline]
