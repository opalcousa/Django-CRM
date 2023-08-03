import csv
import os
import io

class CSVWriter:
    def __init__(self, filename):
        self.filename = filename

    def write(self, orders):
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['Order Number', 'Order Date', 'Customer Name', 'Products Purchased', 'Total Purchase Price'])
        for order in orders:
            writer.writerow([order.id, order.order_date, order.customer_name, ', '.join([str(p) for p in order.product_names]), order.total_price])
        return output.getvalue()
