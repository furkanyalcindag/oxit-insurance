from django.db import models

from insurance.models import Teklif


class KrediKarti(models.Model):
    PESIN = 'PEŞİN'
    TAKSIT = 'TAKSİT'

    odeme_choices = (
        (PESIN, 'PEŞİN'),
        (TAKSIT, 'TAKSİT'),
    )



    teklif = models.ForeignKey(Teklif, on_delete=models.CASCADE)
    ad_soyad = models.CharField(max_length=512, null=True, blank=True)
    kart_no = models.CharField(max_length=512, null=True, blank=True)
    banka = models.CharField(max_length=512, null=True, blank=True)
    cv2 = models.CharField(max_length=512, null=True, blank=True)
    gecerlilik_tarihi = models.CharField(max_length=512, null=True, blank=True)
    aciklama = models.TextField(max_length=10000, null=True, blank=True)
    odeme_sekli = models.CharField(max_length=128, choices=odeme_choices, null=True, blank=True)
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
