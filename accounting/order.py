from django.db import models
from accounting.product import Product

class Order(models.Model):
    """Represents an order with an ID, customer name, product, quantity, and order date."""
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateField()

    def get_total_price(self):
        """Returns the total price of the order."""
        return self.product.get_price(self.quantity)
