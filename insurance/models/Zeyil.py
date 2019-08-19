from django.db import models

from insurance.models.Acente import Acente


class Zeyil(models.Model):
    beklemede = 'Beklemede'
    isleme_alindi = 'İşleme Alındı'
    onaylandi = 'Onaylandı'
    reddedildi = 'Reddedildi'

    STATE_CHOICES = (
        (beklemede, 'Beklemede'),
        (isleme_alindi, 'İşleme Alındı'),
        (onaylandi, 'Onaylandı'),
        (reddedildi, 'Reddedildi')
    )

    TYPE_CHOICES = (

        ("Satıştan İptal", "Satıştan İptal"),
        ("Plaka Zeyili", "Plaka Zeyili"),
        ("Mükerrer Zeyil", "Mükerrer Zeyil"),
        ("Genel Zeyil", "Genel Zeyil")

    )
    police_numarasi = models.CharField(max_length=322, blank=True, null=True)
    acente = models.ForeignKey(Acente, on_delete=models.CASCADE)
    sigorta_sirketi = models.CharField(max_length=322, blank=True, null=True)
    durum = models.CharField(null=True, max_length=122, blank=True, choices=STATE_CHOICES, default=beklemede)
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')
    brans = models.CharField(max_length=233, null=True, blank=True)
    zeyil_turu = models.CharField(null=True, max_length=122, blank=True, choices=TYPE_CHOICES)
    aciklama = models.TextField(max_length=10000, null=True, blank=True)
