from django.db import models

# Create your models here.
from django.db import models

class Depense(models.Model):
    CATEGORIES = [
        ('NOURRITURE', 'Nourriture'),
        ('TRANSPORT', 'Transport'),
        ('LOGEMENT', 'Logement'),
        ('LOISIRS', 'Loisirs'),
        ('AUTRE', 'Autre'),
    ]
    
    titre = models.CharField(max_length=100)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.CharField(max_length=20, choices=CATEGORIES, default='AUTRE')
    date = models.DateField(auto_now_add=True)  # La date d'aujourd'hui automatique
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.titre} - {self.montant} CFA"