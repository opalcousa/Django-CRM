import math

class PurchaseOrderGenerator:
    def __init__(self, product_base_cost=20, aloe_vera_cost=30, hemp_oil_cost=60, bottle_cost=0.70):
        self.product_base_cost = product_base_cost
        self.aloe_vera_cost = aloe_vera_cost
        self.hemp_oil_cost = hemp_oil_cost
        self.bottle_cost = bottle_cost
        self.serial_number = 100000000

    def generate_purchase_order(self, orders):
        purchase_orders = []
        for order in orders:
            total_bottles = order.get('quantity', 0)  
            total_gallons = total_bottles / 16
            total_aloe_vera = total_gallons * 300 / 3785.41
            total_hemp_oil = total_gallons / 256
            total_cost = (total_gallons * self.product_base_cost +
                          total_aloe_vera * self.aloe_vera_cost +
                          total_hemp_oil * self.hemp_oil_cost +
                          total_bottles * self.bottle_cost)
            cost_per_unit = total_cost / total_bottles if total_bottles else 0
            self.serial_number += 1
            purchase_orders.append({
                'product_id': order.get('product_id', 'default_product_id'),
                'product_base_gallons': round(total_gallons, 2),
                'aloe_vera_gallons': round(total_aloe_vera, 2),
                'hemp_oil_gallons': round(total_hemp_oil, 2),
                'bottles': round(total_bottles, 2),
                'total_cost': round(total_cost, 2),
                'cost_per_unit': round(cost_per_unit, 2),
                'serial_number': self.serial_number
            })
        return purchase_orders
