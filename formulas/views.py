from django.shortcuts import render, redirect
from .models import Formula
from .forms import FormulaForm  # new

def index(request):
    # List all formulas
    formulas = Formula.objects.all()
    return render(request, 'formulas/index.html', {'formulas': formulas})  # updated path

def detail(request, formula_id):
    # Show details of a specific formula
    formula = get_object_or_404(Formula, pk=formula_id)
    return render(request, 'formulas/detail.html', {'formula': formula})  # updated path

def create(request):
    # Handle the creation of a new formula
    if request.method == 'POST':
        form = FormulaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formulas:index')
    else:
        form = FormulaForm()

    return render(request, 'formulas/create.html', {'form': form})

def update(request, formula_id):
    # Handle the update of a formula
    formula = Formula.objects.get(pk=formula_id)
    if request.method == 'POST':
        form = FormulaForm(request.POST, instance=formula)
        if form.is_valid():
            form.save()
            return redirect('formulas:detail', formula_id=formula.id)
    else:
        form = FormulaForm(instance=formula)

    return render(request, 'formulas/update.html', {'form': form})

def delete(request, formula_id):
    # Handle the deletion of a formula
    formula = Formula.objects.get(pk=formula_id)
    if request.method == 'POST':
        formula.delete()
        return redirect('formulas:index')

    return render(request, 'formulas/delete.html', {'formula': formula})


