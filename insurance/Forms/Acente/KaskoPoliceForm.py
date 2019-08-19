from django.forms import ModelForm, forms

from insurance.models import TrafikPolice, KaskoPolice


class KaskoPoliceForm(ModelForm):
    police_file = forms.FileField()

    class Meta:
        model = KaskoPolice
        fields = ('police_file','police_numarasi')
