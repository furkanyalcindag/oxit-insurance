from django.forms import ModelForm, forms

from insurance.models import TrafikPolice


class TrafikPoliceForm(ModelForm):
    police_file = forms.FileField()

    class Meta:
        model = TrafikPolice
        fields = ('police_file',)
