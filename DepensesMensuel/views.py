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