# ana acente
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from insurance.Forms.Acente.KaskoForm import KaskoForm
from insurance.Forms.Acente.KaskoPoliceForm import KaskoPoliceForm
from insurance.Forms.Acente.KrediKartiForm import KrediKartiForm
from insurance.Forms.Acente.MusteriForm import MusteriForm
from insurance.Forms.Acente.TrafikForm import TrafikForm
from insurance.Forms.Acente.TrafikPoliceForm import TrafikPoliceForm
from insurance.models import TrafikSigortasi, TeklifTalep, SigortaSirketi, Teklif, Ayar, TrafikPolice, KrediKarti, \
    KaskoSigortasi, KaskoPolice
from insurance.models.TalepObject import TalepObject
from insurance.models.TalepTeklifObject import TalepTeklifObject


@login_required
def kasko_bekleyen_talepler(request):
    teklif_talepleri = TeklifTalep.objects.filter(cevaplandi=False).filter(sigortaTipi__tip="Kasko").order_by('-id')

    talep_objeleri = []

    for talep in teklif_talepleri:
        sigorta = KaskoSigortasi.objects.get(id=talep.sigorta_id)
        obje = TalepObject(id=talep.id, acente=talep.acente, sigorta_tipi=talep.sigortaTipi, sigorta=sigorta,
                           sigorta_sirketleri=talep.sigorta_Sirketleri.all(), cevaplandi=talep.cevaplandi,
                           olusturulma_tarihi=talep.creationDate)
        talep_objeleri.append(obje)

    return render(request, 'AnaAcente/kasko/kasko_bekleyen_talepler.html', {'talepler': talep_objeleri})


@login_required
def kasko_cevaplanan_talepler(request):
    teklif_talepleri = TeklifTalep.objects.filter(cevaplandi=True).filter(sigortaTipi__tip="Kasko").order_by('-id')

    talep_objeleri = []

    for talep in teklif_talepleri:
        sigorta = KaskoSigortasi.objects.get(id=talep.sigorta_id)
        teklif = Teklif.objects.filter(teklif_talep=talep, teklif_kabul=True,police_mi=False)
        if teklif.count() != 0:
            obje = TalepTeklifObject(id=talep.id, acente=talep.acente, sigorta_tipi=talep.sigortaTipi, sigorta=sigorta,
                                     sigorta_sirketleri=talep.sigorta_Sirketleri.all(), cevaplandi=talep.cevaplandi,
                                     olusturulma_tarihi=talep.creationDate, teklif=teklif)
            talep_objeleri.append(obje)

    return render(request, 'AnaAcente/kasko/kasko_bekleyen_talepler.html', {'talepler': talep_objeleri})


@login_required
def KaskoTeklifVer(request, pk):
    teklif_talep = TeklifTalep.objects.get(pk=pk)

    sigorta = KaskoSigortasi.objects.get(id=teklif_talep.sigorta_id)

    musteriForm = MusteriForm(request.POST or None, instance=sigorta.sigortali)

    kaskoForm = KaskoForm(request.POST or None, instance=sigorta)

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

        return redirect("insurance:bekleyen-kasko-istek")

    if teklif is None:
        return render(request, 'AnaAcente/kasko/kasko_teklif_olustur.html',
                      {'musteri_form': musteriForm, 'kasko_form': kaskoForm,
                       'sirketler': teklif_talep.sigorta_Sirketleri.all()})
    else:
        return render(request, 'AnaAcente/kasko/kasko_teklif_olustur.html',
                      {'musteri_form': musteriForm, 'kasko_form': kaskoForm,
                       'sirketler': teklif_talep.sigorta_Sirketleri.all(), 'teklifler': teklif})


@login_required
def kaskoTeklifIncele(request, pk):
    teklif_talep = TeklifTalep.objects.get(pk=pk)

    sigorta = KaskoSigortasi.objects.get(id=teklif_talep.sigorta_id)

    musteriForm = MusteriForm(request.POST or None, instance=sigorta.sigortali)

    kaskoForm = KaskoForm(request.POST or None, instance=sigorta)

    teklif = Teklif.objects.filter(teklif_talep=teklif_talep)

    return render(request, 'AnaAcente/kasko/kasko_teklif_incele.html',
                  {'musteri_form': musteriForm, 'kasko_form': kaskoForm,
                   'sirketler': teklif_talep.sigorta_Sirketleri.all(), 'teklifler': teklif})


@login_required
def kasko_police_olustur(request, pk):
    teklif = Teklif.objects.filter(pk=pk)
    sigorta = KaskoSigortasi.objects.get(id=teklif[0].teklif_talep.sigorta_id)

    odeme = KrediKarti.objects.get(teklif=teklif[0])

    musteriForm = MusteriForm(request.POST or None, instance=sigorta.sigortali)

    kaskoForm = KaskoForm(request.POST or None, instance=sigorta)

    odeme_form = KrediKartiForm(request.POST or None, instance=odeme)

    policeForm = KaskoPoliceForm()

    teklif_p = teklif[0]

    if request.method == "POST":
        policeForm = KaskoPoliceForm(request.POST, request.FILES)
        if policeForm.is_valid():

            teklif_p.police_mi = True
            teklif_p.prim_tutari = (teklif_p.teklif_tutari * int(Ayar.objects.get(name="kasko_prim").value)) / 100
            teklif_p.save()
            police = KaskoPolice(teklif=teklif_p, police_file=policeForm.cleaned_data['police_file'],
                                 police_numarasi=policeForm.cleaned_data['police_numarasi'])
            police.save()
            messages.success(request, 'Poliçe başarıyla oluşturuldu.')
            return redirect("insurance:kasko-acente-policeleri")
        else:
            messages.warning(request, 'Form alanlarını kontrol ediniz')
    return render(request, 'AnaAcente/kasko/kasko_police_olustur.html',
                  {'musteri_form': musteriForm, 'kasko_form': kaskoForm,
                   'police_form': policeForm, 'sirketler': teklif[0].sigorta_sirket, 'teklifler': teklif,
                   'kart_form': odeme_form})


@login_required
def acente_policeleri(request):
    policeler = KaskoPolice.objects.all()
    return render(request, "AnaAcente/kasko/acente-policeleri.html", {"policeler": policeler})
