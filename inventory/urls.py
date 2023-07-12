from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [
    path('', views.InventoryHomeView.as_view(), name='inventory_home'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/new/', views.ProductCreateView.as_view(), name='new_product'),
    path('stocks/', views.StockListView.as_view(), name='stocks'),
    path('stocks/new/', views.StockCreateView.as_view(), name='new_stock'),
    path('suppliers/', views.SupplierListView.as_view(), name='suppliers'),
    path('suppliers/new/', views.SupplierCreateView.as_view(), name='new_supplier'),
    path('purchase_orders/', views.PurchaseOrderListView.as_view(), name='purchase_orders'),
    path('purchase_orders/new/', views.PurchaseOrderCreateView.as_view(), name='new_purchase_order'),
    path('sales_orders/', views.SalesOrderListView.as_view(), name='sales_orders'),
    path('sales_orders/new/', views.SalesOrderCreateView.as_view(), name='new_sales_order'),
]
