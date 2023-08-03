from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Order, Product
from .order_generator import OrderGenerator
import datetime
from .order_generator import OrderGenerator
import datetime

def index_view(request):
    return JsonResponse({"message": "Welcome to the Accounting Application"})

def dashboard(request):
    total_orders = Order.objects.count()
    total_products = Product.objects.count()
    total_sales = sum(order.product.price * order.quantity for order in Order.objects.all())
    total_profit_loss = total_sales - sum(order.product.cost * order.quantity for order in Order.objects.all())
    return JsonResponse({
        'total_orders': total_orders,
        'total_products': total_products,
        'total_sales': total_sales,
        'total_profit_loss': total_profit_loss,
    })

def orders(request):
    try:
        orders = Order.objects.all()
        orders_list = list(orders.values())
        return JsonResponse(orders_list, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return JsonResponse({
        'id': order.id,
        'customer_name': order.customer_name,
        'product': order.product.name,
        'quantity': order.quantity,
        'order_date': order.order_date
    })

def products(request):
    try:
        products = Product.objects.all()
        products_list = list(products.values())
        return JsonResponse(products_list, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return JsonResponse({
        'id': product.id,
        'name': product.name,
        'price': product.price
    })

def generate_orders(request):
    order_generator = OrderGenerator(datetime.date.today() - datetime.timedelta(days=30), datetime.date.today())
    generated_orders = order_generator.generate_orders(10)
    for order in generated_orders:
        product_names = order['product_names'].split(', ')
        for product_name in product_names:
            product, created = Product.objects.get_or_create(name=product_name)
            Order.objects.create(customer_name=order['customer_name'], product=product, order_date=order['order_date'], total_price=order['total_price'])
    return JsonResponse({"message": "Orders generated and saved to the database."})

def generate_orders(request):
    order_generator = OrderGenerator(datetime.date.today() - datetime.timedelta(days=30), datetime.date.today())
    generated_orders = order_generator.generate_orders(10)
    for order in generated_orders:
        product_names = order['product_names'].split(', ')
        for product_name in product_names:
            product, created = Product.objects.get_or_create(name=product_name)
            Order.objects.create(customer_name=order['customer_name'], product=product, order_date=order['order_date'], total_price=order['total_price'])
    return JsonResponse({"message": "Orders generated and saved to the database."})

def profit_loss(request):
    # TODO: Implement the logic for the profit and loss statement
    return JsonResponse({"message": "Profit & Loss Statement"})
