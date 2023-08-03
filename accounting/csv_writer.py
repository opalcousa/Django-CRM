import csv
import os

class CSVWriter:
    def __init__(self, filename):
        self.filename = filename

    import io

    def write(self, orders):
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['Customer Name', 'Product Name', 'Order Date', 'Total Price'])
        total_revenue = 0
        for order in orders:
            order = list(order)
            if isinstance(order[1], list):
                order[1] = ', '.join(order[1])
            if isinstance(order[3], str) and order[3].isdigit():
                order[3] = int(order[3])
            if isinstance(order[3], int):
                total_revenue += order[3]
            writer.writerow(order)
        return output.getvalue()
