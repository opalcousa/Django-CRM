from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Product, Stock, Supplier, PurchaseOrder, SalesOrder

class ProductListView(generic.ListView):
    model = Product

class StockListView(generic.ListView):
    model = Stock

class SupplierListView(generic.ListView):
    model = Supplier

class PurchaseOrderListView(generic.ListView):
    model = PurchaseOrder

class SalesOrderListView(generic.ListView):
    model = SalesOrder
