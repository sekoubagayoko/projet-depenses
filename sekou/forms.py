
# from django import forms
from .models import Sekou

class SekouForm(forms.ModelForm):
    class Meta:
        model = Sekou
        fields = ['nom', 'email', 'poste', 'salaire']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'input w-full',  # ← corrigé : "input" au lieu de "inpu"
                'placeholder': 'Nom'
            }),
            'email': forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder': 'Email'
            }),
            'poste': forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder': 'Poste'
            }),
            'salaire': forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder': 'Salaire'
            }),
        }