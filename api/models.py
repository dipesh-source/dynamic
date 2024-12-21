from django.db import models
from django.utils.timezone import now


# 1. Product Management
class Product(models.Model):
    name = models.CharField(max_length=255)
    base_price = models.FloatField()
    product_type = models.CharField(
        max_length=50,
        choices=[("seasonal", "Seasonal"), ("bulk", "Bulk"), ("premium", "Premium")],
    )

    def get_price(self, quantity=1):
        if self.product_type == "seasonal":
            return self.base_price * 0.8  # 20% discount for seasonal products
        elif self.product_type == "bulk":
            if 10 <= quantity <= 20:
                return self.base_price * 0.95
            elif 21 <= quantity <= 50:
                return self.base_price * 0.9
            elif quantity > 50:
                return self.base_price * 0.85
        elif self.product_type == "premium":
            return self.base_price * 1.15  # 15% markup for premium products
        return self.base_price


# 2. Discount Management
class Discount(models.Model):
    name = models.CharField(max_length=255)
    priority = models.IntegerField()
    discount_type = models.CharField(
        max_length=50,
        choices=[
            ("percentage", "Percentage"),
            ("fixed", "Fixed"),
            ("tiered", "Tiered"),
        ],
    )
    value = models.FloatField()

    def apply_discount(self, price, quantity=1):
        if self.discount_type == "percentage":
            return price * (1 - self.value / 100)
        elif self.discount_type == "fixed":
            return max(price - self.value, 0)
        elif self.discount_type == "tiered":
            if 500 <= price <= 1000:
                return price * 0.95  # 5% discount
            elif price > 1000:
                return price * 0.9  # 10% discount
        return price


class Order(models.Model):
    created_at = models.DateTimeField(default=now)
    products = models.ManyToManyField(Product, through="OrderProduct")
    discounts = models.ManyToManyField(Discount, blank=True)

    def calculate_total(self):
        total = 0
        product_quantities = self.orderproduct_set.all()

        for pq in product_quantities:
            total += pq.product.get_price(pq.quantity) * pq.quantity

        for discount in self.discounts.order_by("priority"):
            total = discount.apply_discount(total)

        return total


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
