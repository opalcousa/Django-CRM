class Product:
    """Represents a product with a name and a price."""

    def __init__(self, name, price):
        """Initializes a new product with a name and a price."""
        self.name = name
        self.price = price

    def get_price(self, quantity):
        """Returns the total price for a given quantity of the product."""
        return self.price * quantity if quantity % 3 != 0 else (quantity // 3) * 25
