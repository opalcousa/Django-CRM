from django import forms

class OrderGeneratorForm(forms.Form):
    start_date = forms.DateField(widget=forms.SelectDateWidget())
    end_date = forms.DateField(widget=forms.SelectDateWidget())
    num_orders = forms.IntegerField(min_value=1)
