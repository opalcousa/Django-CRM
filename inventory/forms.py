from django import forms
from .models import Product, Stock, Supplier, PurchaseOrder, SalesOrder

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description']

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['product', 'quantity']

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_info']

class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ['product', 'supplier', 'quantity']

class SalesOrderForm(forms.ModelForm):
    class Meta:
        model = SalesOrder
        fields = ['product', 'quantity']
