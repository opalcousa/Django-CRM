from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ingredient, Formulation

class IngredientListView(ListView):
    model = Ingredient
    template_name = 'templates/ingredient_list.html'  # replace with your template
    context_object_name = 'ingredients'

class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = 'templates/ingredient_detail.html'  # replace with your template

class IngredientCreateView(CreateView):
    model = Ingredient
    fields = ['field1', 'field2']  # replace with your model fields
    template_name = 'templates/ingredient_form.html'  # replace with your template

class IngredientUpdateView(UpdateView):
    model = Ingredient
    fields = ['field1', 'field2']  # replace with your model fields
    template_name = 'templates/ingredient_form.html'  # replace with your template

class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = 'templates/ingredient_confirm_delete.html'  # replace with your template
    success_url = '/ingredients/'  # replace with your success url


class FormulationListView(ListView):
    model = Formulation
    template_name = 'templates/formulation_list.html'  # replace with your template
    context_object_name = 'formulations'

class FormulationDetailView(DetailView):
    model = Formulation
    template_name = 'templates/formulation_detail.html'  # replace with your template

class FormulationCreateView(CreateView):
    model = Formulation
    fields = ['field1', 'field2']  # replace with your model fields
    template_name = 'templates/formulation_form.html'  # replace with your template

class FormulationUpdateView(UpdateView):
    model = Formulation
    fields = ['field1', 'field2']  # replace with your model fields
    template_name = 'templates/formulation_form.html'  # replace with your template

class FormulationDeleteView(DeleteView):
    model = Formulation
    template_name = 'templates/formulation_confirm_delete.html'  # replace with your template
    success_url = '/formulations/'  # replace with your success url
