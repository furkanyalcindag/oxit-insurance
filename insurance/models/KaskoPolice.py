from django.db import models

from insurance.models import Teklif


class KaskoPolice(models.Model):
    teklif = models.ForeignKey(Teklif, on_delete=models.CASCADE)
    police_numarasi = models.CharField(max_length=128, null=True, blank=True)
    police_file = models.FileField(upload_to='uploads/kasko/%Y/%m/%d/')

    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')
