# ana acente
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from insurance.Forms.Acente.MusteriForm import MusteriForm
from insurance.Forms.Acente.TrafikForm import TrafikForm
from insurance.Forms.Acente.TrafikPoliceForm import TrafikPoliceForm
from insurance.models import TrafikSigortasi, TeklifTalep, SigortaSirketi, Teklif, Ayar, TrafikPolice
from insurance.models.TalepObject import TalepObject

@login_required
def bekleyen_talepler(request):
    teklif_talepleri = TeklifTalep.objects.filter(cevaplandi=False).order_by('-id')

    talep_objeleri = []

    for talep in teklif_talepleri:
        sigorta = TrafikSigortasi.objects.get(id=talep.sigorta_id)
        obje = TalepObject(id=talep.id, acente=talep.acente, sigorta_tipi=talep.sigortaTipi, sigorta=sigorta,
                           sigorta_sirketleri=talep.sigorta_Sirketleri.all(), cevaplandi=talep.cevaplandi,
                           olusturulma_tarihi=talep.creationDate)
        talep_objeleri.append(obje)

    return render(request, 'AnaAcente/bekleyen_talepler.html', {'talepler': talep_objeleri})

@login_required
def cevaplanan_talepler(request):
    teklif_talepleri = TeklifTalep.objects.filter(cevaplandi=True).order_by('-id')

    talep_objeleri = []

    for talep in teklif_talepleri:
        sigorta = TrafikSigortasi.objects.get(id=talep.sigorta_id)
        obje = TalepObject(id=talep.id, acente=talep.acente, sigorta_tipi=talep.sigortaTipi, sigorta=sigorta,
                           sigorta_sirketleri=talep.sigorta_Sirketleri.all(), cevaplandi=talep.cevaplandi,
                           olusturulma_tarihi=talep.creationDate)
        talep_objeleri.append(obje)

    return render(request, 'AnaAcente/bekleyen_talepler.html', {'talepler': talep_objeleri})

@login_required
def trafikTeklifVer(request, pk):
    teklif_talep = TeklifTalep.objects.get(pk=pk)

    sigorta = TrafikSigortasi.objects.get(id=teklif_talep.sigorta_id)

    musteriForm = MusteriForm(request.POST or None, instance=sigorta.sigortali)

    trafikForm = TrafikForm(request.POST or None, instance=sigorta)

    teklif = Teklif.objects.filter(teklif_talep=teklif_talep)

    if request.method == "POST":

        list = []
        sirketler = SigortaSirketi.objects.all()
        for key in request.POST.keys():

            for sirket in sirketler:
                if sirket.sirket_adi == key:
                    teklif = Teklif(teklif_talep=teklif_talep, sigorta_sirket=sirket, teklif_tutari=request.POST[key])
                    teklif.save()
                    teklif_talep.cevaplandi = True
                    teklif_talep.save()

        messages.success(request, "Teklif Oluşturuldu")

        return redirect("insurance:bekleyen-trafik-istek")

    if teklif is None:
        return render(request, 'AnaAcente/trafik_teklif_olustur.html',
                      {'musteri_form': musteriForm, 'trafik_form': trafikForm,
                       'sirketler': teklif_talep.sigorta_Sirketleri.all()})
    else:
        return render(request, 'AnaAcente/trafik_teklif_olustur.html',
                      {'musteri_form': musteriForm, 'trafik_form': trafikForm,
                       'sirketler': teklif_talep.sigorta_Sirketleri.all(), 'teklifler': teklif})

@login_required
def trafikTeklifIncele(request, pk):
    teklif_talep = TeklifTalep.objects.get(pk=pk)

    sigorta = TrafikSigortasi.objects.get(id=teklif_talep.sigorta_id)

    musteriForm = MusteriForm(request.POST or None, instance=sigorta.sigortali)

    trafikForm = TrafikForm(request.POST or None, instance=sigorta)

    teklif = Teklif.objects.filter(teklif_talep=teklif_talep)

    return render(request, 'AnaAcente/trafik_teklif_incele.html',
                  {'musteri_form': musteriForm, 'trafik_form': trafikForm,
                   'sirketler': teklif_talep.sigorta_Sirketleri.all(), 'teklifler': teklif})

@login_required
def trafik_police_olustur(request, pk):
    teklif = Teklif.objects.filter(pk=pk)
    sigorta = TrafikSigortasi.objects.get(id=teklif[0].teklif_talep.sigorta_id)

    musteriForm = MusteriForm(request.POST or None, instance=sigorta.sigortali)

    trafikForm = TrafikForm(request.POST or None, instance=sigorta)

    policeForm = TrafikPoliceForm()

    teklif_p = teklif[0]

    if request.method == "POST":

        policeForm = TrafikPoliceForm(request.POST, request.FILES)
        teklif_p.police_mi = True
        teklif_p.prim_tutari = (teklif_p.teklif_tutari * int(Ayar.objects.get(name="trafik_prim").value))/100
        teklif_p.save()
        police = TrafikPolice(teklif=teklif_p,police_file=policeForm.cleaned_data['police_file'])
        police.save()
        return redirect("insurance:acente-policeleri")

    return render(request, 'AnaAcente/trafik_police_olustur.html',
                  {'musteri_form': musteriForm, 'trafik_form': trafikForm,
                   'police_form': policeForm, 'sirketler': teklif[0].sigorta_sirket, 'teklifler': teklif})

@login_required
def acente_policeleri(request):
    policeler = TrafikPolice.objects.all()
    return render(request,"AnaAcente/acente-policeleri.html", {"policeler":policeler})