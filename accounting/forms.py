from django import forms

from django.forms.widgets import DateInput

class OrderGeneratorForm(forms.Form):
    start_date = forms.DateField(widget=DateInput(attrs={'type': 'date', 'max': datetime.date.today()}))
    end_date = forms.DateField(widget=DateInput(attrs={'type': 'date', 'max': datetime.date.today()}))
    num_orders = forms.IntegerField(min_value=1)
