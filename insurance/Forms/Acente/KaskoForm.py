from django import forms
from django.forms import ModelForm

from insurance.models import TrafikSigortasi, KaskoSigortasi


class KaskoForm(ModelForm):
    class Meta:
        model = KaskoSigortasi
        fields = ( 'arac_plaka','yeni_plaka', 'belge_seri_no', 'kullanim_tarzi', 'arac_marka','arac_marka_kodu' ,'arac_tipi', 'model_yili',
                  'arac_faturali', 'fatura_tarihi',
                  'arac_bedeli', 'motor_numarasi', 'sasi_numarasi', 'imm', 'koltuk_sayisi', 'tescil_tarihi', 'aksesuar_bedeli','kasa_bedeli_kasa_tipi','lpg_bedeli', 'tasinan_emtea_ve_cinsi','aciklama')

        widgets = {
            'arac_plaka': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Araç Plakası', 'required': 'required','readonly':'readonly'}),
            'yeni_plaka': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Yeni Plaka', 'readonly':'readonly'}),
            'belge_seri_no': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Belge Seri No', 'readonly':'readonly'}),
            'kullanim_tarzi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kullanım Tarzı','readonly':'readonly'}),
            'arac_marka': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Araç Markası','readonly':'readonly'}),
            'arac_marka_kodu': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Araç Markası Kodu','readonly':'readonly'}),
            'arac_tipi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Araç Tipi','readonly':'readonly'}),
            'model_yili': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Model Yılı','readonly':'readonly'}),
            'arac_faturali': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                 'style': 'width: 100%;', 'disabled':'disabled'}),
            'fatura_tarihi': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker1', 'autocomplete': 'off',
                       'onkeydown': 'return false', 'readonly':'readonly'}),
            'arac_bedeli': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Araç Bedeli', 'readonly':'readonly'}),
            'motor_numarasi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Motor Numarası', 'readonly':'readonly'}),
            'sasi_numarasi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Şasi Numarası', 'readonly':'readonly'}),
            'imm': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'IMM', 'readonly':'readonly'}),
            'koltuk_sayisi': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Koltuk Sayısı','readonly':'readonly'}),
            'tescil_tarihi': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker2', 'autocomplete': 'off',
                       'onkeydown': 'return false', 'readonly':'readonly'}),
            'aksesuar_bedeli': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Aksesuar Bedeli','readonly':'readonly'}),
            'lpg_bedeli': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'LPG Bedeli', 'readonly':'readonly'}),
            'tasinan_emtea_ve_cinsi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Taşınan emtea ve cinsi', 'readonly':'readonly'}),
            'aciklama': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Açıklama', 'readonly':'readonly'}),

        }
