from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from datetime import datetime
from .models import Depense
from .forms import DepenseForm

def liste_depenses(request):
    depenses = Depense.objects.all()
    
    # --- FILTRE PAR MOIS ---
    mois_filtre = request.GET.get('mois')
    if mois_filtre:
        try:
            annee, mois = mois_filtre.split('-')
            depenses = depenses.filter(date__year=int(annee), date__month=int(mois))
        except (ValueError, TypeError):
            pass
    
    # Calcul du total
    total = depenses.aggregate(Sum('montant'))['montant__sum'] or 0
    
    # Répartition par catégorie
    categories = {}
    for d in depenses:
        categories[d.categorie] = categories.get(d.categorie, 0) + float(d.montant)
    
    # Mois actuel par défaut
    mois_actuel = datetime.now().strftime('%Y-%m')
    
    return render(request, 'depenses/liste.html', {
        'depenses': depenses,
        'total': total,
        'categories': categories,
        'mois_filtre': mois_filtre or mois_actuel,
    })

def ajouter_depense(request):
    if request.method == 'POST':
        form = DepenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_depenses')
    else:
        form = DepenseForm()
    return render(request, 'depenses/ajouter.html', {'form': form})

def modifier_depense(request, pk):
    depense = get_object_or_404(Depense, pk=pk)
    if request.method == 'POST':
        form = DepenseForm(request.POST, instance=depense)
        if form.is_valid():
            form.save()
            return redirect('liste_depenses')
    else:
        form = DepenseForm(instance=depense)
    return render(request, 'depenses/modifier.html', {'form': form, 'depense': depense})

def supprimer_depense(request, pk):
    depense = get_object_or_404(Depense, pk=pk)
    if request.method == 'POST':
        depense.delete()
        return redirect('liste_depenses')
    return render(request, 'depenses/supprimer.html', {'depense': depense})