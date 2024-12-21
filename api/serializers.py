from rest_framework import serializers
from api.models import *


# Serializers
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    products = ProductSerializer(many=True)  # Nested serializer
    discounts = DiscountSerializer(many=True)  # Nested serializer

    class Meta:
        model = Order
        fields = ["created_at", "products", "discounts", "total_price"]

    def get_total_price(self, obj):
        return obj.calculate_total()
