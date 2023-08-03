import datetime
from .order_generator import OrderGenerator
from .save_records import save_records
from .profit_loss_statement import main as calculate_profit_loss

def main():
    # Generate orders
    start_date = datetime.date(2021, 1, 1)
    end_date = datetime.date(2021, 12, 31)
    order_generator = OrderGenerator(start_date, end_date)
    orders = order_generator.generate_orders(100)

    # Save records
    order_fieldnames = ['order_date', 'customer_name', 'product_names', 'total_price']
    save_records(orders, 'orders.csv', order_fieldnames)

    # Calculate profit/loss
    calculate_profit_loss()

if __name__ == '__main__':
    main()
