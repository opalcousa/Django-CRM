from django.urls import path
from .views import IngredientListView, IngredientDetailView, IngredientCreateView, IngredientUpdateView, IngredientDeleteView, formulationListView, formulationDetailView, formulationCreateView, formulationUpdateView, formulationDeleteView

appName = 'formulation'
urlpatterns = [
    path('ingredients/', IngredientListView.as_view(), name='ingredient-list'),
    path('ingredients/<int:pk>/', IngredientDetailView.as_view(), name='ingredient-detail'),
    path('ingredients/new/', IngredientCreateView.as_view(), name='ingredient-create'),
    path('ingredients/<int:pk>/edit/', IngredientUpdateView.as_view(), name='ingredient-update'),
    path('ingredients/<int:pk>/delete/', IngredientDeleteView.as_view(), name='ingredient-delete'),
    path('formulation/', formulationListView.as_view(), name='formulation-list'),
    path('formulation/<int:pk>/', formulationDetailView.as_view(), name='formulation-detail'),
    path('formulation/new/', formulationCreateView.as_view(), name='formulation-create'),
    path('formulation/<int:pk>/edit/', formulationUpdateView.as_view(), name='formulation-update'),
    path('formulation/<int:pk>/delete/', formulationDeleteView.as_view(), name='formulation-delete'),
]
