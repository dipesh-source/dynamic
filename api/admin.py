from django.contrib import admin
from api.models import Product, Discount, Order, OrderProduct

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    pass
