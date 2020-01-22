from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.signals import m2m_changed
from django.shortcuts import render, redirect

import insurance
from insurance.Forms.KrediKartiForm import KrediKartiForm
from insurance.Forms.MusteriForm import MusteriForm
from insurance.Forms.SirketSecForm import SirketSecForm
from insurance.Forms.TrafikForm import TrafikForm
from insurance.models import Musteri, Acente, SigortaSirketi, TeklifTalep, SigortaTipi, TrafikSigortasi, Teklif, \
    TrafikPolice, KrediKarti
from insurance.models.TalepObject import TalepObject


@login_required
def teklif_olustur_trafik(request):
    musteri_form = MusteriForm()
    trafik_form = TrafikForm()
    sirket_sec = SirketSecForm()

    if request.method == "POST":
        musteri_form = MusteriForm(request.POST)
        trafik_form = TrafikForm(request.POST)
        sirket_sec = SirketSecForm(request.POST)

        sirket = []

        user = request.user

        acente = Acente.objects.get(user=user)
        sigorta_tipi = SigortaTipi.objects.get(tip='Trafik')

        for s in request.POST.getlist('sirketler'):
            sirket.append(SigortaSirketi.objects.get(sirket_adi=s))

        if musteri_form.is_valid() and trafik_form.is_valid():
            musteri = None
            trafik = None
            try:
                musteri = musteri_form.save(commit=False)
                musteri.acente = acente
                musteri.save()
            except:
                messages.warning(request, "Müşteri formunu kontrol ediniz")
                return redirect("insurance:trafik-teklif-iste")

            try:
                trafik_sigorta = trafik_form.save(commit=False)
                trafik_sigorta.sigortali = musteri
                trafik = trafik_sigorta.save()
            except Exception as ex:
                messages.warning(request, "Form alanlarını kontrol ediniz")
                instance = Musteri.objects.get(id=musteri.id).delete()
                return redirect("insurance:trafik-teklif-iste")

            try:
                teklif_talep = TeklifTalep(acente=acente, sigortaTipi=sigorta_tipi, sigorta_id=trafik_sigorta.id)
                teklif_talep.save()
                for sirket in sirket:
                    teklif_talep.sigorta_Sirketleri.add(sirket)
                messages.success(request, "Teklif talebi başarıyla oluşturuldu")
                teklif_talep.save()
                return redirect('insurance:trafik-teklif-talepleri')
            except Exception as e:

                messages.warning(request, "Form alanlarını kontrol ediniz")
                instanceMusteri = Musteri.objects.get(id=musteri.id).delete()
                trafik = TrafikSigortasi.objects.get(id=trafik.id).delete()
                return redirect(request, "insurance:trafik-teklif-iste")

    return render(request, 'TrafikSigortasi/trafik-sigortasi-teklif-iste.html',
                  {'musteri_form': musteri_form, 'trafik_form': trafik_form, 'sirket_sec': sirket_sec})


# acente
@login_required
def teklif_taleplerim(request):
    acente = Acente.objects.get(user=request.user)
    teklif_talepleri = TeklifTalep.objects.filter(acente=acente)

    talep_objeleri = []

    for talep in teklif_talepleri:
        sigorta = TrafikSigortasi.objects.get(id=talep.sigorta_id)
        obje = TalepObject(id=talep.id, acente=acente, sigorta_tipi=talep.sigortaTipi, sigorta=sigorta,
                           sigorta_sirketleri=talep.sigorta_Sirketleri.all(), cevaplandi=talep.cevaplandi,
                           olusturulma_tarihi=talep.creationDate)

        if talep.cevaplandi:
            teklif = Teklif.objects.filter(teklif_talep=talep)
            if teklif[0].kapandi == False:
                talep_objeleri.append(obje)

        else:
            talep_objeleri.append(obje)

    return render(request, 'TrafikSigortasi/teklif-talepleri.html', {'talepler': talep_objeleri})


@login_required
def teklif_cevapla(request, pk):
    teklif_talep = TeklifTalep.objects.get(pk=pk)

    sigorta = TrafikSigortasi.objects.get(id=teklif_talep.sigorta_id)

    kart_form = KrediKartiForm()

    musteriForm = insurance.Forms.Acente.MusteriForm.MusteriForm(request.POST or None, instance=sigorta.sigortali)

    trafikForm = insurance.Forms.Acente.TrafikForm.TrafikForm(request.POST or None, instance=sigorta)

    teklif = Teklif.objects.filter(teklif_talep=teklif_talep)

    if request.method == 'POST':

        kart_form = KrediKartiForm(request.POST)

        if kart_form.is_valid():

            teklif = Teklif.objects.get(id=int(request.POST['teklif']))
            if teklif.teklif_kabul == True:
                return redirect("insurance:trafik-teklif-talepleri")
            teklif.teklif_kabul = True
            teklif.kapandi = True

            teklif.save()

            kredi_karti = KrediKarti(teklif=teklif, kart_no=kart_form.cleaned_data.get('kart_no'),
                                     ad_soyad=kart_form.cleaned_data.get('ad_soyad'),
                                     gecerlilik_tarihi=kart_form.cleaned_data.get('gecerlilik_tarihi'),
                                     cv2=kart_form.cleaned_data.get('cv2'),
                                     odeme_sekli=kart_form.cleaned_data.get('odeme_sekli'),
                                     banka=kart_form.cleaned_data.get('banka'))

            kredi_karti.save()

            teklifler = Teklif.objects.filter(teklif_talep=teklif_talep)

            for teklifd in teklifler:
                teklifd.kapandi = True
                teklifd.save()

            messages.success(request, "Teklif başarıyla kabul edildi")
            return redirect("insurance:trafik-teklif-talepleri")
        else:
            return render(request, 'TrafikSigortasi/teklif-onayla.html',
                          {'musteri_form': musteriForm, 'trafik_form': trafikForm, 'kart_form': kart_form,
                           'sirketler': teklif_talep.sigorta_Sirketleri.all(), 'teklifler': teklif})

    return render(request, 'TrafikSigortasi/teklif-onayla.html',
                  {'musteri_form': musteriForm, 'trafik_form': trafikForm, 'kart_form': kart_form,
                   'sirketler': teklif_talep.sigorta_Sirketleri.all(), 'teklifler': teklif})


@login_required
def acente_policeleri(request):
    acente = Acente.objects.get(user=request.user)
    policeler = TrafikPolice.objects.filter(teklif__teklif_talep__acente=acente)
    return render(request, "TrafikSigortasi/acente-trafik-policelerim.html", {"policeler": policeler})
