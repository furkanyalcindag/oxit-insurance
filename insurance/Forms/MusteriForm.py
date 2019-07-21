from django.forms import ModelForm

from insurance.models import Musteri


class MusteriForm(ModelForm):
    class Meta:
        model = Musteri
        fields = {}