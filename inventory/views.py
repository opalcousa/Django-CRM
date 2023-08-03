from django.shortcuts import render
from django.views import generic
from .models import Product, Stock, Supplier
from .forms import ProductForm, StockForm, SupplierForm

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

class ProductUpdateView(generic.edit.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/product_form.html'
    success_url = '/inventory/products/'

class ProductDeleteView(generic.edit.DeleteView):
    model = Product
    template_name = 'inventory/product_confirm_delete.html'
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

class StockUpdateView(generic.edit.UpdateView):
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

class SupplierUpdateView(generic.edit.UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'inventory/supplier_form.html'
    success_url = '/inventory/suppliers/'

class StockDeleteView(generic.edit.DeleteView):
    model = Stock
    template_name = 'inventory/stock_confirm_delete.html'
    success_url = '/inventory/stocks/'

class SupplierDeleteView(generic.edit.DeleteView):
    model = Supplier
    template_name = 'inventory/supplier_confirm_delete.html'
    success_url = '/inventory/suppliers/'
