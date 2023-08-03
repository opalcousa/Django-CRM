from django.urls import path
from . import views

app_name = 'accounting'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('orders/', views.orders, name='orders'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('products/', views.products, name='products'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('profit_loss/', views.profit_loss, name='profit_loss'),
    path('index/', views.index_view, name='index'),  # Corrected line
    path('generate_orders/', views.generate_orders, name='generate_orders'),
    path('export_orders/', views.export_orders, name='export_orders'),
]
