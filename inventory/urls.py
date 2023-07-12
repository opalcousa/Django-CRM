from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='products'),
    path('stocks/', views.StockListView.as_view(), name='stocks'),
    path('suppliers/', views.SupplierListView.as_view(), name='suppliers'),
    path('purchase_orders/', views.PurchaseOrderListView.as_view(), name='purchase_orders'),
    path('sales_orders/', views.SalesOrderListView.as_view(), name='sales_orders'),
]
