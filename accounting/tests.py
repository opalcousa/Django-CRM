from django.test import TestCase
from .models import Product, Order
from decimal import Decimal
from datetime import date

class OrderModelTest(TestCase):
    def test_saving_and_retrieving_orders(self):
        product = Product()
        product.name = 'Test Product'
        product.price = Decimal('9.99')
        product.save()

        order = Order()
        order.customer_name = 'Test Customer'
        order.product = product
        order.quantity = 5
        order.order_date = date.today()
        order.save()

        saved_orders = Order.objects.all()
        self.assertEqual(saved_orders.count(), 1)

        saved_order = saved_orders[0]
        self.assertEqual(saved_order.customer_name, 'Test Customer')
        self.assertEqual(saved_order.product, product)
        self.assertEqual(saved_order.quantity, 5)
        self.assertEqual(saved_order.order_date, date.today())
