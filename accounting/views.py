from django.shortcuts import render
from accounting.models import Order

def dashboard(request):
    orders = Order.objects.all()
    return render(request, 'dashboard.html', {'orders': orders})
