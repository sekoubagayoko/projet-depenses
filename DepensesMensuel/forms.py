from django import forms
from .models import Depense

class DepenseForm(forms.ModelForm):
    class Meta:
        model = Depense
        fields = ['titre', 'categorie', 'montant']  # ← 'date' retiré
        widgets = {
            'titre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Titre de la dépense'
            }),
            'categorie': forms.Select(attrs={
                'class': 'form-select'
            }),
            'montant': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Montant en CFA',
                'step': '0.01'
            }),
        }