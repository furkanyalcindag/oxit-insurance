from django import forms

from insurance.models import SigortaSirketi


class SirketSecForm(forms.Form):
    sirketler = forms.ModelMultipleChoiceField(queryset=SigortaSirketi.objects.values_list('sirket_adi', flat=True),
                                               widget=forms.Select(
                                                   attrs={'class': 'form-control select2 ',
                                                          'placeholder': 'Mesaj İçeriği', 'multiple': 'multiple',
                                                          'data-placeholder': 'Sigorta Şİrketlerini Seçiniz.',
                                                          'required': 'required'}))
