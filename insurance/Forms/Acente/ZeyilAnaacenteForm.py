from django import forms
from django.forms import ModelForm

from insurance.models import Zeyil


class ZeyilAnaacenteForm(ModelForm):
    class Meta:
        model = Zeyil
        fields = {'police_numarasi', 'sigorta_sirketi', 'brans', 'zeyil_turu', 'aciklama', 'durum'}

        widgets = {

            'police_numarasi': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Poliçe Numarası', 'value': '', 'readonly': 'readonly',
                       'required': 'required'}),

            'sigorta_sirketi': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Sigorta Şirketi', 'value': '', 'readonly': 'readonly',
                       'required': 'required'}),

            'brans': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Sigorta Türü', 'value': '', 'readonly': 'readonly',
                       'required': 'required'}),

            'zeyil_turu': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                              'style': 'width: 100%;', 'disabled': 'disabled'}),

            'aciklama': forms.Textarea(
                attrs={'class': 'form-control ', 'placeholder': 'Açıklama', 'readonly': 'readonly'}),

            'durum': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                         'style': 'width: 100%;'}),

        }
