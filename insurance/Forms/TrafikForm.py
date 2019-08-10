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
                attrs={'class': 'form-control ', 'placeholder': 'Araç Plakası', 'required': 'required'}),
            'belge_seri_no': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Belge Seri No'}),
            'kullanim_tarzi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kullanım Tarzı'}),
            'arac_marka': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Araç Markası'}),
            'arac_tipi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Araç Tipi'}),
            'model_yili': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Model Yılı'}),
            'arac_faturali': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                 'style': 'width: 100%;'}),
            'fatura_tarihi': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker1', 'autocomplete': 'off',
                       'onkeydown': 'return false'}),
            'arac_bedeli': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Araç Bedeli'}),
            'motor_numarasi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Motor Numarası'}),
            'sasi_numarasi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Şasi Numarası'}),
            'imm': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'IMM'}),
            'koltuk_sayisi': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Koltuk Sayısı'}),
            'tescil_tarihi': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker2', 'autocomplete': 'off',
                       'onkeydown': 'return false'}),

        }
