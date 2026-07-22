from django.db import models

class Sekou(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    poste = models.CharField(max_length=100)
    salaire = models.DecimalField(max_digits=10, decimal_places=2)


