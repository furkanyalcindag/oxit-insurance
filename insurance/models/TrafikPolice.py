from django.db import models

from insurance.models import Teklif


class TrafikPolice(models.Model):
    teklif = models.ForeignKey(Teklif, on_delete=models.CASCADE)
    police_file = models.FileField(upload_to='uploads/%Y/%m/%d/')

    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')
