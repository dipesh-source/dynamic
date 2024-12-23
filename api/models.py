from django.db import models
from django.utils.timezone import now


from datetime import date
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    base_price = models.FloatField()
    product_type = models.CharField(
        max_length=50,
        choices=[("seasonal", "Seasonal"), ("bulk", "Bulk"), ("premium", "Premium")],
    )

    def get_price(self, quantity=1):
        raise NotImplementedError("Subclasses must implement the `get_price` method.")

    class Meta:
        abstract = True


class SeasonalProduct(Product):
    def get_price(self, quantity=1):
        current_month = date.today().month
        winter_months = [12, 1, 2]  # December, January, February
        if current_month in winter_months:
            return self.base_price * 0.8  # 20% off during winter
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
