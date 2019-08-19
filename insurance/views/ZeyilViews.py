from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from insurance.Forms.Acente.ZeyilAnaacenteForm import ZeyilAnaacenteForm
from insurance.Forms.ZeyilForm import ZeyilForm
from insurance.models import Acente
from insurance.models.Zeyil import Zeyil


@login_required
def zeyil_olustur(request):
    zeyilForm = ZeyilForm()

    if request.method == 'POST':
        zeyilForm = ZeyilForm(request.POST)

        if zeyilForm.is_valid():

            zeyil = zeyilForm.save(commit=False)
            zeyil.acente = Acente.objects.get(user=request.user)
            zeyil.save()
            messages.success(request, "Zeyil Talebi başarıyla oluşturuldu")
            return redirect('insurance:acente-zeyil-talepleri')
        else:
            messages.warning(request, "Form alanlarını kontrol ediniz.")

    return render(request, "Zeyil/zeyil-talebi-olustur.html", {'zeyil_form': zeyilForm})


@login_required
def zeyil_taleplerim(request):
    acente = Acente.objects.get(user=request.user)
    zeyiller = Zeyil.objects.filter(acente=acente).order_by('-id')

    return render(request, "Zeyil/acente-zeyil-taleplerim.html", {'zeyil_talepler': zeyiller})


@login_required
def zeyil_talepleri_tum(request):
    zeyiller = Zeyil.objects.all().order_by('-id')

    return render(request, "AnaAcente/zeyil/zeyil-talepleri.html", {'zeyil_talepler': zeyiller})


@login_required
def zeyil_durum_guncelle(request, pk):


    zeyil = Zeyil.objects.get(pk=pk)
    copy=zeyil
    zeyilForm = ZeyilAnaacenteForm(request.POST or None, instance=copy)

    if request.method == 'POST':

        if zeyilForm.is_valid():
            zeyil = Zeyil.objects.get(pk=pk)
            zeyil.durum = zeyilForm.cleaned_data.get('durum')

            zeyil.save()
            messages.success(request, "Zeyil Talebi durumu başarıyla güncellendi")
            return redirect('insurance:zeyil-istekleri')
        else:
            messages.warning(request, "Form alanlarını kontrol ediniz.")

    return render(request, "AnaAcente/zeyil/zeyil-talebi-durum-guncelle.html", {'zeyil_form': zeyilForm})
