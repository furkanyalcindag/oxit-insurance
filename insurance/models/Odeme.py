from django.db import models

from insurance.models import Acente


class Odeme(models.Model):
    acente = models.ForeignKey(Acente, on_delete=models.CASCADE)
    odeme_tutari = models.DecimalField(max_digits=10, decimal_places=2)
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')