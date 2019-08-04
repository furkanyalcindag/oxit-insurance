from django.db import models

from insurance.models import Acente, SigortaTipi, SigortaSirketi


class TeklifTalep(models.Model):
    acente = models.ForeignKey(Acente, on_delete=models.CASCADE, null=True)
    sigortaTipi = models.ForeignKey(SigortaTipi, on_delete=models.CASCADE, null=True)
    sigorta_id = models.IntegerField(null=True, blank=True)
    sigorta_Sirketleri = models.ManyToManyField(SigortaSirketi)
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')