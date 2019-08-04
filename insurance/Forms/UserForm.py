from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class UserForm(ModelForm):
    #confirm_password = forms.CharField( widget=forms.PasswordInput(
     #   attrs={'class': 'form-control', 'placeholder': 'Şifre Tekrarı'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'is_active')
        widgets = {
            'first_name': forms.TextInput( attrs={'class': 'form-control ', 'placeholder': ' Adı', 'value': '', 'required':'required'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': ' Soyadı', 'required':'required'}),
            'username': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'E-mail', 'required':'required'}),
            'email': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Email'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'iCheck-helper'}),
            #'password': forms.PasswordInput(attrs={'class': 'form-control ', 'placeholder': 'Şifre',}),



        }
