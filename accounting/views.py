from django.shortcuts import render
from accounting.order import Order

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
