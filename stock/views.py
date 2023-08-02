from django.shortcuts import render
from django.views import generic
from .models import Product, Stock, Supplier
from .forms import ProductForm, StockForm, SupplierForm

class InventoryHomeView(generic.TemplateView):
    template_name = 'stock/home.html'

class ProductListView(generic.ListView):
    model = Product

class ProductDetailView(generic.DetailView):
    model = Product

class ProductCreateView(generic.edit.CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'stock/product_form.html'
    success_url = '/stock/products/'

class ProductUpdateView(generic.edit.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'stock/product_form.html'
    success_url = '/stock/products/'

class StockListView(generic.ListView):
    model = Stock

class StockDetailView(generic.DetailView):
    model = Stock

class StockCreateView(generic.edit.CreateView):
    model = Stock
    form_class = StockForm
    template_name = 'stock/stock_form.html'
    success_url = '/stock/stocks/'

class StockUpdateView(generic.edit.UpdateView):
    model = Stock
    form_class = StockForm
    template_name = 'stock/stock_form.html'
    success_url = '/stock/stocks/'

class SupplierListView(generic.ListView):
    model = Supplier

class SupplierDetailView(generic.DetailView):
    model = Supplier

class SupplierCreateView(generic.edit.CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'stock/supplier_form.html'
    success_url = '/stock/suppliers/'
