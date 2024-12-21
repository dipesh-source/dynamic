# Description: This file contains the views for the API.

# rest_framework
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# API
from api.models import *
from api.serializers import *


# ViewSets
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=["get"])
    def get_price(self, request, pk=None):
        product = self.get_object()
        quantity = int(request.query_params.get("quantity", 1))
        return Response({"price": product.get_price(quantity)})


class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=True, methods=["get"])
    def total_price(self, request, pk=None):
        order = self.get_object()
        return Response({"total_price": order.calculate_total()})
