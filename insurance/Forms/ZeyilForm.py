from django import forms
from django.forms import ModelForm

from insurance.models import Zeyil


class ZeyilForm(ModelForm):
    class Meta:
        model = Zeyil
        fields = {'police_numarasi', 'sigorta_sirketi','brans','zeyil_turu','aciklama'}

        widgets = {

            'police_numarasi': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Poliçe Numarası', 'value': '', 'required': 'required'}),

            'sigorta_sirketi': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Sigorta Şirketi', 'value': '', 'required': 'required'}),

            'brans': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Sigorta Türü', 'value': '', 'required': 'required'}),

            'zeyil_turu': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                            'style': 'width: 100%;'}),

            'aciklama': forms.Textarea(attrs={'class': 'form-control ', 'placeholder': 'Açıklama'}),

        }