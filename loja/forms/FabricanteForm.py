from django import forms
from loja.models import Fabricante

class FabricanteForm(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = ['nome', 'site']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'site': forms.URLInput(attrs={'class': 'form-control'}),
        }