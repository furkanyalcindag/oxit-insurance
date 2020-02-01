from django import forms
from django.forms import ModelForm

from insurance.models import TrafikSigortasi, KaskoSigortasi


class KaskoForm(ModelForm):
    class Meta:
        model = KaskoSigortasi
        fields = ('arac_plaka', 'kullanim_tarzi', 'arac_marka', 'arac_tipi', 'model_yili',
                  'arac_bedeli', 'belge_seri_no',
                  'motor_numarasi', 'sasi_numarasi', 'koltuk_sayisi', 'tescil_tarihi', 'aksesuar_bedeli',
                  'kasa_bedeli_kasa_tipi', 'lpg_bedeli', 'tasinan_emtea_ve_cinsi', 'aciklama')

        widgets = {
            'arac_plaka': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Araç Plakası', 'required': 'required'}),

            'kullanim_tarzi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kullanım Tarzı'}),
            'arac_marka': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Araç Markası'}),
            'belge_seri_no': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Belge Seri No'}),

            'arac_tipi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Araç Tipi'}),
            'model_yili': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Model Yılı'}),

            'arac_bedeli': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Araç Bedeli'}),
            'motor_numarasi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Motor Numarası'}),
            'sasi_numarasi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Şasi Numarası'}),

            'koltuk_sayisi': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Koltuk Sayısı'}),
            'tescil_tarihi': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker2', 'autocomplete': 'off',
                       'onkeydown': 'return false'}),
            'aksesuar_bedeli': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Aksesuar Bedeli'}),
            'lpg_bedeli': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'LPG Bedeli'}),
            'tasinan_emtea_ve_cinsi': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Taşınan emtea ve cinsi'}),
            'aciklama': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Açıklama'}),

        }
