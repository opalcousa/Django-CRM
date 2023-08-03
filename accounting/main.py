import datetime
from .order_generator import OrderGenerator
from .purchase_order_generator import PurchaseOrderGenerator
from .save_records import save_records
from .profit_loss_statement import main as calculate_profit_loss

def main():
    # Generate orders
    start_date = datetime.date(2021, 1, 1)
    end_date = datetime.date(2021, 12, 31)
    order_generator = OrderGenerator(start_date, end_date)
    orders = order_generator.generate_orders(100)

    # Generate purchase orders
    purchase_order_generator = PurchaseOrderGenerator()
    purchase_orders = purchase_order_generator.generate_purchase_order(orders)

    # Save records
    order_fieldnames = ['order_date', 'customer_name', 'product_names', 'total_price']
    save_records(orders, 'orders.csv', order_fieldnames)

    purchase_order_fieldnames = ['serial_number', 'cost_per_unit', 'product_id', 'hemp_oil_gallons', 'aloe_vera_gallons', 'bottles', 'product_base_gallons', 'total_cost']
    save_records(purchase_orders, 'purchase_orders.csv', purchase_order_fieldnames)

    # Calculate profit/loss
    calculate_profit_loss()

if __name__ == '__main__':
    main()
