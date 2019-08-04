from django.shortcuts import render

from insurance.models import Ayar


def ayar_liste(request):
    ayarlar= Ayar.objects.all().order_by("id")
    return render(request,"Ayar/ayar-listesi.html",{"ayarlar":ayarlar})