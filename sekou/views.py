from django.shortcuts import render , redirect , get_object_or_404
from .models import Sekou
from .forms import SekouForm
def liste_sekou(request):
    
    sekou= Sekou.objects.all()
    return render(request , 'sekou/list.html' ,{'sekou':sekou})
def ajouter_sekou (request):
    form = SekouForm(request.POST or None)
    if form.is_valid() :
       form.save()
       return redirect('liste_sekou')
    return render(request , 'sekou/formulaire.html' ,{'form':form})
def modifier_sekou ( request , id) :
    sekou = get_object_or_404(Sekou , id=id)
    form = SekouForm(request.POST or None , instance=sekou)
    if form.is_valid() :
       form.save()
       return redirect('liste_sekou')
    return render(request , 'sekou/formulaire.html' ,{'form':form})
def supprimer_sekou ( request , id) :
    sekou = get_object_or_404(Sekou , id=id)
    if request.method== "POST":
       sekou.delete()
       return redirect('liste_sekou')
    return render(request , 'sekou/confirmer_suppression.html' ,{'sekou':sekou})



