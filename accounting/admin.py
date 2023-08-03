from django.contrib import admin
from accounting.order import Order
from accounting.product import Product

admin.site.register(Product)
admin.site.register(Order)
