from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from insurance.models import Ayar

@login_required
def ayar_liste(request):
    ayarlar= Ayar.objects.all().order_by("id")
    return render(request,"Ayar/ayar-listesi.html",{"ayarlar":ayarlar})