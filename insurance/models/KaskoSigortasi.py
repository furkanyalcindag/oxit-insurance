from django.db import models

from insurance.models import Acente
from insurance.models.Musteri import Musteri


class KaskoSigortasi(models.Model):
    YES = 'Evet'
    NO = 'Hayır'

    fatura_choices = (
        (YES, 'Evet'),
        (NO, 'Hayır'),
    )
    sigortali = models.ForeignKey(Musteri, on_delete=models.CASCADE, null=True)
    acente = models.ForeignKey(Acente, on_delete=models.CASCADE, null=True)
    arac_plaka = models.CharField(max_length=50, blank=True, null=True, verbose_name='Araç Plakası')
    yeni_plaka = models.CharField(max_length=50, blank=True, null=True, verbose_name='Yeni Araç Plakası')
    belge_seri_no = models.CharField(max_length=120, verbose_name='Belge Seri No')
    kullanim_tarzi = models.CharField(max_length=128, verbose_name='Kullanım Tarzı')
    arac_marka = models.TextField(max_length=1024,blank=True, null=True, verbose_name='Araç Markası')
    arac_marka_kodu = models.TextField(max_length=1024, blank=True, null=True, verbose_name='Araç Markası Kodu')
    arac_tipi = models.TextField(blank=True, null=True, verbose_name='Araç Tipi')
    model_yili = models.CharField(max_length=128, null=True, verbose_name='Model Yili')
    arac_faturali = models.CharField(max_length=128, verbose_name='Araç Faturalı mı', choices=fatura_choices, default=NO)
    fatura_tarihi= models.CharField(max_length=128, null=True, verbose_name='Fatura Tarihi')
    arac_bedeli = models.CharField(max_length=128, null=True, blank=True, verbose_name='Araç Bedeli')
    motor_numarasi = models.CharField(max_length=128, null=True, blank=True, verbose_name='Motor Numarası')
    sasi_numarasi = models.CharField(max_length=128, null=True, blank=True, verbose_name='Saşi Numarası')
    imm = models.CharField(max_length=128, null=True, blank=True, verbose_name='IMM')
    koltuk_sayisi= models.CharField(max_length=128, null=True, blank=True, verbose_name='Koltuk Sayısı')
    tescil_tarihi= models.CharField(max_length=128,null=True, verbose_name='Tescil Tarihi')
    aksesuar_bedeli = models.CharField(max_length=128, null=True, blank=True, verbose_name='Aksesuar Bedeli')
    kasa_bedeli_kasa_tipi = models.CharField(max_length=128, null=True, blank=True, verbose_name='Kasa Bedeli')
    lpg_bedeli = models.CharField(max_length=128, null=True, blank=True, verbose_name='LPG Bedeli')
    tasinan_emtea_ve_cinsi = models.CharField(max_length=128, null=True, blank=True, verbose_name='Taşınan Emtea ve Cinsi')
    aciklama = models.TextField(max_length=10024, blank=True, null=True, verbose_name='Açıklama')
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')


