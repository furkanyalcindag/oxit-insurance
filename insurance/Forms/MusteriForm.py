from django import forms
from django.forms import ModelForm

from insurance.models import Musteri


class MusteriForm(ModelForm):
    class Meta:
        model = Musteri
        fields = {'adi', 'soyadi', 'telefon', 'adres', 'meslek', 'tc', 'vergi_no', }

        widgets = {

            'adi': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Adı', 'value': '', 'required': 'required'}),

            'soyadi': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Soyadı', 'value': '', 'required': 'required'}),

            'telefon': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Telefon', 'value': '' }),


            'adres': forms.Textarea(attrs={'class': 'form-control ', 'placeholder': 'Adres'}),

            'meslek': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Meslek', 'value': ''}),

            'tc': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'T.C. No', 'value': '', 'required': 'required'}),

            'vergi_no': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Vergi No:', 'value': ''}),



        }
