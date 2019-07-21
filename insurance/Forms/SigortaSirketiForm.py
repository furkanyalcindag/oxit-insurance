from django.forms import ModelForm

from insurance.models import SigortaSirketi


class SigortaSirketiForm(ModelForm):
    class Meta:
        model = SigortaSirketi
        fields = {'sirket_adi'}
