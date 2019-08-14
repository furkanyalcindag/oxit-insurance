from django.db import models

from insurance.models import Acente
from oxiterp.settings import base


class Musteri(models.Model):
    MALE = 'Erkek'
    FEMALE = 'Kadın'

    GENDER_CHOICES = (
        (MALE, 'Erkek'),
        (FEMALE, 'Kadın'),
    )
    adi = models.CharField(max_length=100, verbose_name='Adı')
    soyadi = models.CharField(max_length=100, verbose_name='Soyadı')
    telefon = models.CharField(max_length=120, verbose_name='Telefon Numarası')
    cinsiyet = models.CharField(max_length=128, verbose_name='Cinsiyeti', choices=GENDER_CHOICES, default=FEMALE)
    adres = models.TextField(max_length=512,blank=True, null=True, verbose_name='Adres')
    meslek = models.TextField(blank=True, null=True, verbose_name='Mesleği')
    tc = models.CharField(max_length=128, null=True, blank=True, verbose_name='T.C. Kimlik Numarası')
    vergi_no = models.CharField(max_length=128, null=True, blank=True, verbose_name='Vergi Numarası')
    dogum_tarihi = models.DateField(null=True, verbose_name='Doğum Tarihi')
    acente = models.ForeignKey(Acente, on_delete=models.CASCADE, default=None, null=True)
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')
