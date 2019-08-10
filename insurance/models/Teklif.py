from django.db import models

from insurance.models.TeklifTalep import TeklifTalep
from insurance.models.SigortaSirketi import SigortaSirketi


class Teklif(models.Model):
    teklif_talep = models.ForeignKey(TeklifTalep, on_delete=models.CASCADE, null=True, blank=True)
    sigorta_sirket = models.ForeignKey(SigortaSirketi, on_delete=models.CASCADE, null=True, blank=True)
    teklif_tutari = models.DecimalField(max_digits=10, decimal_places=2)
    teklif_kabul = models.BooleanField(default=False)
    police_mi = models.BooleanField(default=False)
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')
    prim_tutari = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)
    kapandi = models.BooleanField(default=False)
