from django.urls import path
from . import views

app_name = 'formulas'  # This is new

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:formula_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:formula_id>/update/', views.update, name='update'),
    path('<int:formula_id>/delete/', views.delete, name='delete'),
]
