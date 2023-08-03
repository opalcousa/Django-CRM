from django.contrib import admin
from .models import Product
from accounting.order import Order

admin.site.register(Product)
admin.site.register(Order)
