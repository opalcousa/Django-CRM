from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, Stock, Supplier, PurchaseOrder, SalesOrder

admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Supplier)
admin.site.register(PurchaseOrder)
admin.site.register(SalesOrder)
