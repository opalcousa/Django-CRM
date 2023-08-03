import csv

def calculate_total(filename):
    with open(filename, 'r') as file:                         
         reader = csv.reader(file)                             
         next(reader)  # Skip the header row                   
         total = sum(float(row[3]) for row in reader)
    return total

def main():
    total_sales = calculate_total('reports/orders.csv')
    total_purchase_orders = calculate_total('reports/purchase_orders.csv')
    profit_loss = total_sales - total_purchase_orders

    print('Profit & Loss Statement')
    print('-----------------------')
    print(f'Total Sales: ${total_sales:.2f}')
    print(f'Total Purchase Orders: ${total_purchase_orders:.2f}')
    print(f'Profit/Loss: ${profit_loss:.2f}')

if __name__ == '__main__':
    main()
