from django.shortcuts import render
from accounting.order import Order
from django.shortcuts import render
from .order_generator import OrderGenerator
import datetime

def dashboard(request):
    orders = Order.objects.all()
    return render(request, 'dashboard.html', {'orders': orders})

def orders(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'order_detail.html', {'order': order})

def profit_loss(request):
    total_sales = 1000  # Replace with actual calculation
    total_purchase_orders = 500  # Replace with actual calculation
    profit_loss = total_sales - total_purchase_orders  # Replace with actual calculation
    return render(request, 'profit_loss.html', {'total_sales': total_sales, 'total_purchase_orders': total_purchase_orders, 'profit_loss': profit_loss})
from django.shortcuts import render
from .order_generator import OrderGenerator
from .forms import OrderGeneratorForm
from .csv_writer import CSVWriter
from django.http import HttpResponse

def generate_orders(request):
    if request.method == 'POST':
        form = OrderGeneratorForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            num_orders = form.cleaned_data['num_orders']
            order_generator = OrderGenerator(start_date, end_date)
            orders = order_generator.generate_orders(num_orders)
            if 'export' in request.POST:
                csv_writer = CSVWriter('orders.csv')
                csv_writer.write(orders)
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="orders.csv"'
                csv_writer.write(orders, response)
                return response
            return render(request, 'accounting/orders.html', {'orders': orders, 'form': form})
    else:
        form = OrderGeneratorForm()
    return render(request, 'accounting/orders.html', {'form': form})
def index_view(request):
    return render(request, 'index.html')