from django import forms
from django.forms import ModelForm

from insurance.models import SigortaSirketi


class SigortaSirketiForm(ModelForm):
    class Meta:
        model = SigortaSirketi
        fields = {'sirket_adi','aktif'}

        widgets = {

            'sirket_adi': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Şirket Adı', 'value': '', 'required': 'required'}),

            'aktif': forms.CheckboxInput(attrs={'class': 'iCheck-helper'}),

        }
