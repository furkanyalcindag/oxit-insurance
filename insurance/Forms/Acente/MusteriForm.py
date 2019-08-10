from django import forms
from django.forms import ModelForm

from insurance.models import Musteri


class MusteriForm(ModelForm):
    class Meta:
        model = Musteri
        fields = {'adi', 'soyadi', 'telefon', 'cinsiyet', 'adres', 'meslek', 'tc', 'vergi_no', 'dogum_tarihi'}


        widgets = {

            'adi': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Adı', 'value': '', 'readonly':'readonly'}),

            'soyadi': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Soyadı', 'value': '', 'readonly':'readonly'}),

            'telefon': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Telefon', 'value': '', 'readonly':'readonly' }),

            'cinsiyet': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                            'style': 'width: 100%;',  'disabled':'disabled', 'readonly':'readonly'}),

            'adres': forms.Textarea(attrs={'class': 'form-control ', 'placeholder': 'Adres', 'readonly':'readonly'}),

            'meslek': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Adres', 'value': '', 'readonly':'readonly'}),

            'tc': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'T.C. No', 'value': '', 'required': 'required', 'readonly':'readonly'}),

            'vergi_no': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Vergi No:', 'value': '', 'readonly':'readonly'}),

            'dogum_tarihi': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker','placeholder': 'Doğum Tarihi' ,'autocomplete': 'off',
                       'onkeydown': 'return false', 'readonly':'readonly'}),

        }
