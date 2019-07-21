#tekif alınacak acenteler
from django.db import models
from django.contrib.auth.models import User
from django import *

class Acente(models.Model):
    BOTTOM = 'ANA ACENTE'
    TOP = 'ALT ACENTE'

    Acente_CHOICES = (
        (BOTTOM, 'ANA ACENTE'),
        (TOP, 'ALT ACENTE'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vergi_no = models.CharField(max_length=128, verbose_name="Vergi No", null=True, blank=True)
    telefon = models.CharField(max_length=120, verbose_name='Telefon Numarası')
    acente_adi = models.TextField(max_length=128, verbose_name='Acente Adi', null=True, blank=True)
    adres = models.TextField(max_length=512, verbose_name='Adres', null=True, blank=True)
    #alt_or_ana = models.CharField(max_length=128, verbose_name='ACENTE ÇEŞİDİ', choices=Acente_CHOICES, default=TOP)
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')

