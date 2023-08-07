from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers

from carrello.models import Product, CartItem, Cart


class UserSerializer(serializers.ModelSerializer):
    password = serializers.HiddenField(default="password")

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class ProductSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, obj):
        return Product.objects.get_total_price(obj.category)

    class Meta:
        model = Product
        fields = "__all__"


class SimpleProductWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id',)


class CartItemSerializer(serializers.ModelSerializer):
    method_field = serializers.SerializerMethodField()
    product = ProductSerializer(many=False, read_only=True)

    def get_method_field(self, obj):
        """
        Dimostrazione di method field
        """
        return f"method attribute {obj.id}"

    class Meta:
        model = CartItem
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    user = UserSerializer(many=False, read_only=True)
    products = ProductSerializer(many=True, read_only=False, required=False)

    def create(self, validated_data):
        """
        Salva i dati che arrivano cosi'
        {'name': 'Prodotto 2', 'description': 'Descrizione prodotto 2', 'price': 19.99}
        """
        products = validated_data.pop('products', [])
        with transaction.atomic():
            cart = Cart.objects.create(**validated_data)
            for product_data in products:
                product, _ = Product.objects.get_or_create(**product_data)
                CartItem.objects.create(cart=cart, product=product)
            return cart

    class Meta:
        model = Cart
        fields = "__all__"
