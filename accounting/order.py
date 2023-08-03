from accounting.product import Product

class Order:
    """Represents an order with an ID, customer name, product, quantity, and order date."""

    def __init__(self, id, customer_name, product, quantity, order_date):
        """Initializes a new order with an ID, customer name, product, quantity, and order date."""
        self.id = id
        self.customer_name = customer_name
        self.product = product
        self.quantity = quantity
        self.order_date = order_date

    def get_total_price(self):
        """Returns the total price of the order."""
        return self.product.get_price(self.quantity)
