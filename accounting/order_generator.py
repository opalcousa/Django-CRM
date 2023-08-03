import random
from faker import Faker
import numpy as np


class OrderGenerator:
    def __init__(self, start_date, end_date):
        self.faker = Faker()
        self.start_date = start_date
        self.end_date = end_date
        self.PRODUCTS = ['Shampoo', 'Conditioner', 'Body Wash', 'Lotion']
        self.PRICES = [20, 30, 40, 50]
        self.customers = []

    def _get_product_probabilities(self):
        probabilities = [0.2] * len(self.PRODUCTS)
        shampoo_index = self.PRODUCTS.index('Shampoo')
        conditioner_index = self.PRODUCTS.index('Conditioner')
        probabilities[shampoo_index] = probabilities[conditioner_index] = 0.3
        return probabilities

    def _get_order_quantity(self):
        return np.random.choice([1, 2, 3], p=[0.75, 0.05, 0.20])

    def generate_order(self):
        customer_name = self.faker.name()
        while '.' in customer_name:  # If the name has a title (contains a dot), generate a new one
            customer_name = self.faker.name()
        if not self.customers or random.random() >= 0.17:
            self.customers.append(customer_name)  # Add the new customer to the list
        else:
            customer_name = random.choice(self.customers)
        order_quantity = int(self._get_order_quantity())
        product_names = np.random.choice(self.PRODUCTS, size=order_quantity, replace=False,
                                         p=self._get_product_probabilities())
        quantities = [int(self._get_order_quantity()) for _ in range(len(product_names))]
        product_names = ', '.join(f'{name} ({quantity})' for name, quantity in zip(product_names, quantities))
        order_date = self.faker.date_between_dates(date_start=self.start_date, date_end=self.end_date)
        order_date_str = order_date.strftime('%Y-%m-%d')
        total_quantity = sum(quantities)
        sets_of_three = total_quantity // 3
        individual_products = total_quantity % 3
        total_price = sets_of_three * 25 + individual_products * 10
        return {'customer_name': customer_name, 'product_names': product_names, 'order_date': order_date_str,
                'total_price': total_price}

    def generate_orders(self, n):
        orders = [self.generate_order() for _ in range(n)]
        return orders if orders else []


import datetime
