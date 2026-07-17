
from django import forms
from .models import Sekou
class SekouForm(forms.ModelForm):
    class Meta :
        model = Sekou
        fields = ['nom','email', 'poste', 'salaire']
        widgets={
            'nom':forms.TextInput(attrs={
                'class' : 'inpu w-full',
                'placeholder': 'Nom'
            }),
            'email':forms.TextInput(attrs={
                'class' : 'inpu w-full',
                'placeholder': 'Email'
            }),
            'poste':forms.TextInput(attrs={
                'class' : 'inpu w-full',
                'placeholder': 'Poste'
            }),
            'salaire':forms.TextInput(attrs={
                'class' : 'inpu w-full',
                'placeholder': 'Salaire' 

            }),            

        }