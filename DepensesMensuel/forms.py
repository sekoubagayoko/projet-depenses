from django import forms
from .models import Depense

class DepenseForm(forms.ModelForm):
    class Meta:
        model = Depense
        fields = ['titre', 'montant', 'categorie', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'titre': 'Titre de la dépense',
            'montant': 'Montant (CFA)',
            'categorie': 'Catégorie',
            'description': 'Description (optionnelle)',
        }