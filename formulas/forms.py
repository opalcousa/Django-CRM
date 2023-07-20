from django import forms
from .models import Formula

class FormulaForm(forms.ModelForm):
    class Meta:
        model = Formula
        fields = ['part_number', 'material', 'mass_percent', 'amt_in_batch', 'specific_gravity', 'vol_mL',
                  'vol_percent', 'vol_per_gallon', 'lbs_in_gallon', 'cost_per_pound', 'cost_per_gallon',
                  'cost_per_oz', 'cost_per_bottle']
