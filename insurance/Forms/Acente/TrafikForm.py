from django import forms
from django.forms import ModelForm

from insurance.models import TrafikSigortasi


class TrafikForm(ModelForm):
    class Meta:
        model = TrafikSigortasi
        fields = ( 'arac_plaka', 'belge_seri_no', 'kullanim_tarzi', 'arac_marka', 'arac_tipi', 'model_yili',
                  'arac_faturali', 'fatura_tarihi',
                  'arac_bedeli', 'motor_numarasi', 'sasi_numarasi', 'imm', 'koltuk_sayisi', 'tescil_tarihi')

        widgets = {
            'arac_plaka': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Araç Plakası', 'required': 'required','readonly':'readonly'}),
            'belge_seri_no': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Belge Seri No','readonly':'readonly'}),
            'kullanim_tarzi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kullanım Tarzı', 'readonly':'readonly'}),
            'arac_marka': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Araç Markası', 'readonly':'readonly'}),
            'arac_tipi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Araç Tipi', 'readonly':'readonly'}),
            'model_yili': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Model Yılı', 'readonly':'readonly'}),
            'arac_faturali': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                 'style': 'width: 100%;', 'disabled':'disabled'}),
            'fatura_tarihi': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker1', 'autocomplete': 'off',
                       'onkeydown': 'return false', 'readonly':'readonly'}),
            'arac_bedeli': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Araç Bedeli', 'readonly':'readonly'}),
            'motor_numarasi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Motor Numarası', 'readonly':'readonly'}),
            'sasi_numarasi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Şasi Numarası', 'readonly':'readonly'}),
            'imm': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'IMM', 'readonly':'readonly'}),
            'koltuk_sayisi': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Koltuk Sayısı', 'readonly':'readonly'}),
            'tescil_tarihi': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker2', 'autocomplete': 'on',
                       'onkeydown': 'return false', 'required':'', 'readonly':'readonly'}),

        }
