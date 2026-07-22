# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.liste_depenses, name='liste_depenses'),
#     path('ajouter/', views.ajouter_depense, name='ajouter_depense'),
#     path('modifier/<int:pk>/', views.modifier_depense, name='modifier_depense'),   # <-- NOUVEAU
#     path('supprimer/<int:pk>/', views.supprimer_depense, name='supprimer_depense'), # <-- NOUVEAU
# ]
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.liste_depenses, name='liste_depenses'),
#     path('ajouter/', views.ajouter_depense, name='ajouter_depense'),
#     path('modifier/<int:pk>/', views.modifier_depense, name='modifier_depense'),
#     path('supprimer/<int:pk>/', views.supprimer_depense, name='supprimer_depense'),
#     path('export-csv/', views.export_csv, name='export_csv'),  # <-- NOUVELLE LIGNE
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_depenses, name='liste_depenses'),
    # Les autres fonctionnalités (ajouter, modifier, supprimer, export) seront ajoutées plus tard
]

