from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [
    path('', views.InventoryHomeView.as_view(), name='inventory_home'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/new/', views.ProductCreateView.as_view(), name='new_product'),
    path('products/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='edit_product'),
    path('stocks/', views.StockListView.as_view(), name='stocks'),
    path('stocks/<int:pk>/', views.StockDetailView.as_view(), name='stock_detail'),
    path('stocks/new/', views.StockCreateView.as_view(), name='new_stock'),
    path('stocks/<int:pk>/edit/', views.StockUpdateView.as_view(), name='edit_stock'),
    path('suppliers/', views.SupplierListView.as_view(), name='suppliers'),
    path('suppliers/<int:pk>/', views.SupplierDetailView.as_view(), name='supplier_detail'),
    path('suppliers/new/', views.SupplierCreateView.as_view(), name='new_supplier'),
]
