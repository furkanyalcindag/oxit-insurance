from django.db import models

from insurance.models.Musteri import Musteri
from oxiterp import settings
from oxiterp.settings import base


class TrafikSigortasi(models.Model):
    YES = 'Evet'
    NO = 'Hayır'

    fatura_choices = (
        (YES, 'Evet'),
        (NO, 'Hayır'),
    )
    sigortali = models.ForeignKey(Musteri, on_delete=models.CASCADE, null=True)
    arac_plaka = models.CharField(max_length=50, blank=True, null=True, verbose_name='Araç Plakası')
    belge_seri_no = models.CharField(max_length=120, verbose_name='Belge Seri No')
    kullanim_tarzi = models.CharField(max_length=128, verbose_name='Kullanım Tarzı')
    arac_marka = models.TextField(blank=True, null=True, verbose_name='Araç Markası')
    arac_tipi = models.TextField(blank=True, null=True, verbose_name='Araç Tipi')
    model_yili = models.CharField(max_length=128, null=True, verbose_name='Model Yili')
    arac_faturali = models.CharField(max_length=128, verbose_name='Araç Faturalı mı', choices=fatura_choices,
                                     default=NO)
    fatura_tarihi = models.CharField(max_length=128, null=True, verbose_name='Fatura Tarihi')
    arac_bedeli = models.CharField(max_length=128, null=True, blank=True, verbose_name='Araç Bedeli')
    motor_numarasi = models.CharField(max_length=128, null=True, blank=True, verbose_name='Motor Numarası')
    sasi_numarasi = models.CharField(max_length=128, null=True, blank=True, verbose_name='Şasi Numarası')
    imm = models.CharField(max_length=128, null=True, blank=True, verbose_name='IMM')
    koltuk_sayisi = models.CharField(max_length=128, null=True, blank=True, verbose_name='Koltuk Sayısı')
    tescil_tarihi = models.DateField(null=True, blank=True, verbose_name='Tescil Tarihi')
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')
