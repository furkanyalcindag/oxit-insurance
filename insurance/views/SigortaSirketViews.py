from django.contrib import messages
from django.shortcuts import redirect, render

from insurance.Forms.SigortaSirketiForm import SigortaSirketiForm
from insurance.models import SigortaSirketi


def sirket_ekle(request):
    form = SigortaSirketiForm()
    if request.method == 'POST':
        form = SigortaSirketiForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Şirket Başarıyla Eklendi')
            except:
                messages.warning(request, 'Şirket Eklenemedi')

            return redirect('insurance:sirket-listesi')

    return render(request, 'SigortaSirketi/sigorta-sirketi-ekle.html', {'form': form})


def sirke_guncelle(request, pk):
    sirket = SigortaSirketi.objects.get(pk=pk)

    form = SigortaSirketiForm(request.POST or None, instance=sirket)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Şirket Başarıyla Güncellendi')

            return redirect('insurance:sirket-listesi')

        else:
            messages.warning(request, 'Formu kontrol ediniz')

    return render(request, 'SigortaSirketi/sigorta-sirketi-ekle.html', {'form': form})


def sirket_liste(request):
    sirketler = SigortaSirketi.objects.all()
    return render(request, 'SigortaSirketi/sigorta-sirket-listesi.html', {'sirketler': sirketler})
