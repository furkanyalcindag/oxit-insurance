from django.db import models


class SigortaTipi(models.Model):
    tip = models.CharField(max_length=250, verbose_name='Şirket Adı')

    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')
