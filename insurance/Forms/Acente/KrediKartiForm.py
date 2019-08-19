from django.forms import ModelForm

from insurance.models import Acente, KrediKarti

from django import forms


class KrediKartiForm(ModelForm):
    class Meta:
        model = KrediKarti
        fields = {'ad_soyad', 'kart_no', 'banka', 'cv2', 'gecerlilik_tarihi', 'aciklama', 'odeme_sekli'}

        widgets = {
            'ad_soyad': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Kart Sahibi ', 'value': '', 'required': 'required',
                       'readonly': 'readonly'}),
            'kart_no': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': ' Kart Numarası', 'required': 'required',
                       'readonly': 'readonly'}),
            'banka': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Banka Adı', 'required': 'required',
                       'readonly': 'readonly'}),

            'cv2': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Güvenlik Numarası', 'required': 'required',
                       'readonly': 'readonly'}),

            'gecerlilik_tarihi': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'AA/YY', 'required': 'required',
                       'readonly': 'readonly'}),

            'aciklama': forms.Textarea(
                attrs={'class': 'form-control ', 'placeholder': 'Açıklama', 'readonly': 'readonly'}),

            'odeme_sekli': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                               'style': 'width: 100%;', 'required': 'required',
                                               'readonly': 'readonly', 'disabled':'disabled',}),

            # 'password': forms.PasswordInput(attrs={'class': 'form-control ', 'placeholder': 'Şifre',}),

        }
