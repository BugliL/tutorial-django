from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Product, CartItem, Cart


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


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
    class Meta:
        model = Cart
        fields = "__all__"

        extra_kwargs = {
            'user': {'read_only': True},
            'products': {'read_only': True}
        }
