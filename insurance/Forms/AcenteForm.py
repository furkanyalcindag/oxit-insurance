from django.forms import ModelForm

from insurance.models import Acente

from django import forms
class AcenteForm(ModelForm):

    class Meta:
        model = Acente
        fields = {'acente_adi','adres','telefon','vergi_no'}

        widgets = {
            'acente_adi': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Acente Adı', 'value': '', 'required': 'required'}),
            'vergi_no': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': ' Vergi Numarası', 'required': 'required'}),
            'telefon': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Telefon Numarası', 'required': 'required'}),
            'adres': forms.Textarea(attrs={'class': 'form-control ', 'placeholder': 'Adres', 'required': 'required'}),

            # 'password': forms.PasswordInput(attrs={'class': 'form-control ', 'placeholder': 'Şifre',}),

        }
