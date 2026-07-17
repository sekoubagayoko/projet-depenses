
from django.contrib import admin
from django.urls import path 
from . import views
urlpatterns = [
   
     path("", views.liste_sekou, name="liste_sekou"),
    path("ajouter/", views.ajouter_sekou , name="ajouter_sekou"),
    path("modifier/<int:id>/", views.modifier_sekou , name="modifier_sekou"),
    path("supprimer/<int:id>/", views.supprimer_sekou , name="supprimer_sekou"),
]
