from django.db import models

class Product(models.Model):
    """Represents a product with a name and a price."""
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def get_price(self, quantity):
        """Returns the total price for a given quantity of the product."""
        return self.price * quantity if quantity % 3 != 0 else (quantity // 3) * 25
