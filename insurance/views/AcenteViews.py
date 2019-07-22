from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render

from insurance.Forms.AcenteForm import AcenteForm
from insurance.Forms.UserForm import UserForm
from insurance.models import Acente


@login_required
def acente_ekle(request):
    form = UserForm()
    form_acente = AcenteForm()
    if request.method == 'POST':

        form = UserForm(request.POST)
        form_acente = AcenteForm(request.POST, request.FILES)

        if form.is_valid() and form_acente.is_valid():

            group = Group.objects.filter(name='Acente')
            form.cleaned_data['groups'] = group
            user = form.save(commit=False)
            user.set_password("oxit2016")
            # form.cleaned_data['password'] = make_password(form.cleaned_data['password'])
            user.save()

            acente = Acente(user=user, acente_adi=form_acente.cleaned_data['acente_adi'],
                            vergi_no=form_acente.cleaned_data['vergi_no'],
                            telefon=form_acente.cleaned_data['telefon'],
                            adres=form_acente.cleaned_data['adres'],
                            )
            acente = acente.save()

            return redirect('education:list')
        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')
            # messages.add_message(request, messages.INFO, 'Hello world.')

    return render(request, 'acente-ekle.html', {'form': form, 'form_acente': form_acente})
