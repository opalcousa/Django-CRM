from django.shortcuts import render
from django.views import generic
from .models import Product, Stock, Supplier, PurchaseOrder, SalesOrder
from .forms import ProductForm, StockForm, SupplierForm, PurchaseOrderForm, SalesOrderForm

class InventoryHomeView(generic.TemplateView):
    template_name = 'inventory/home.html'

class ProductListView(generic.ListView):
    model = Product

class ProductDetailView(generic.DetailView):
    model = Product

class ProductCreateView(generic.edit.CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/product_form.html'
    success_url = '/inventory/products/'

class StockListView(generic.ListView):
    model = Stock

class StockDetailView(generic.DetailView):
    model = Stock

class StockCreateView(generic.edit.CreateView):
    model = Stock
    form_class = StockForm
    template_name = 'inventory/stock_form.html'
    success_url = '/inventory/stocks/'

class SupplierListView(generic.ListView):
    model = Supplier

class SupplierDetailView(generic.DetailView):
    model = Supplier

class SupplierCreateView(generic.edit.CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'inventory/supplier_form.html'
    success_url = '/inventory/suppliers/'

class PurchaseOrderListView(generic.ListView):
    model = PurchaseOrder

class PurchaseOrderDetailView(generic.DetailView):
    model = PurchaseOrder

class PurchaseOrderCreateView(generic.edit.CreateView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm
    template_name = 'inventory/purchase_order_form.html'
    success_url = '/inventory/purchase_orders/'

class SalesOrderListView(generic.ListView):
    model = SalesOrder

class SalesOrderDetailView(generic.DetailView):
    model = SalesOrder

class SalesOrderCreateView(generic.edit.CreateView):
    model = SalesOrder
    form_class = SalesOrderForm
    template_name = 'inventory/sales_order_form.html'
    success_url = '/inventory/sales_orders/'
