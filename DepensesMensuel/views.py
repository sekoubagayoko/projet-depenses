from django.db.models import Sum
from django.db.models.functions import ExtractMonth, ExtractYear
import json

def liste_depenses(request):
    depenses = Depense.objects.all().order_by('-date')
    total = depenses.aggregate(Sum('montant'))['montant__sum'] or 0

    # --- Données pour le graphique en barres ---
    # Regrouper les dépenses par mois
    depenses_par_mois = (
        Depense.objects
        .annotate(month=ExtractMonth('date'), year=ExtractYear('date'))
        .values('year', 'month')
        .annotate(total_mois=Sum('montant'))
        .order_by('year', 'month')
    )

    labels = [f"{d['year']}-{d['month']:02d}" for d in depenses_par_mois]
    data = [float(d['total_mois']) for d in depenses_par_mois]

    context = {
        'depenses': depenses,
        'total': total,
        'labels': json.dumps(labels),   # Convertir en JSON pour JS
        'data': json.dumps(data),
    }
    return render(request, 'depenses/liste.html', context)


from django.shortcuts import render, redirect
from .models import Depense
from .forms import DepenseForm  # Assurez-vous d'avoir un formulaire

def ajouter_depense(request):
    if request.method == 'POST':
        form = DepenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_depenses')
    else:
        form = DepenseForm()
    return render(request, 'depenses/ajouter.html', {'form': form})
def ajouter_depense(request):
    if request.method == 'POST':
        titre = request.POST.get('titre')
        categorie = request.POST.get('categorie')
        montant = request.POST.get('montant')
        date = request.POST.get('date')
        Depense.objects.create(
            titre=titre,
            categorie=categorie,
            montant=montant,
            date=date
        )
        return redirect('liste_depenses')
    return render(request, 'depenses/ajouter.html')