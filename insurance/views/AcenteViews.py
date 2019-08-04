from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
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
            try:
                group_acente = Group.objects.get(name='Acente')
            except Group.DoesNotExist:
                obj = Group(name='Acente')
                obj.save()

            group = Group.objects.filter(name='Acente')
            form.cleaned_data['groups'] = group
            form.cleaned_data['email'] = form.cleaned_data['username']
            user = form.save(commit=False)

            user.set_password("sigortahavuzum2019")
            # form.cleaned_data['password'] = make_password(form.cleaned_data['password'])
            user.save()

            acente = Acente(user=user, acente_adi=form_acente.cleaned_data['acente_adi'],
                            vergi_no=form_acente.cleaned_data['vergi_no'],
                            telefon=form_acente.cleaned_data['telefon'],
                            adres=form_acente.cleaned_data['adres'],
                            )
            acente = acente.save()

            messages.success(request, 'Acente Başarıyla Eklendi')
            return redirect('insurance:acente-list')
        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')
            # messages.add_message(request, messages.INFO, 'Hello world.')

    return render(request, 'Acente/acente-ekle.html', {'form': form, 'form_acente': form_acente})


@login_required
def acente_ekle(request):
    form = UserForm()
    form_acente = AcenteForm()
    if request.method == 'POST':

        form = UserForm(request.POST)
        form_acente = AcenteForm(request.POST, request.FILES)

        if form.is_valid() and form_acente.is_valid():
            try:
                group_acente = Group.objects.get(name='Acente')
            except Group.DoesNotExist:
                obj = Group(name='Acente')
                obj.save()

            group = Group.objects.filter(name='Acente')
            form.cleaned_data['groups'] = group
            form.cleaned_data['email'] = form.cleaned_data['username']
            user = form.save(commit=False)

            user.set_password("sigortahavuzum2019")
            # form.cleaned_data['password'] = make_password(form.cleaned_data['password'])
            user.save()

            acente = Acente(user=user, acente_adi=form_acente.cleaned_data['acente_adi'],
                            vergi_no=form_acente.cleaned_data['vergi_no'],
                            telefon=form_acente.cleaned_data['telefon'],
                            adres=form_acente.cleaned_data['adres'],
                            )
            acente = acente.save()

            messages.success(request, 'Acente Başarıyla Eklendi')
            return redirect('insurance:acente-list')
        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')
            # messages.add_message(request, messages.INFO, 'Hello world.')

    return render(request, 'Acente/acente-ekle.html', {'form': form, 'form_acente': form_acente})


@login_required
def acente_list(request):
    acentes = Acente.objects.all().order_by('id')
    return render(request, 'Acente/acente-listesi.html', {'acentes': acentes})


@login_required
def acente_guncelle(request, pk):
    user = User.objects.get(pk=pk)
    acente = Acente.objects.get(user=user)

    form = UserForm(request.POST or None, instance=user)
    form_acente = AcenteForm(request.POST or None, instance=acente)

    if request.method == "POST":
        if all([form.is_valid() and form_acente.is_valid()]):
            form.cleaned_data['email'] = form.cleaned_data['username']
            user = form.save()
            form_acente.save()
            messages.success(request, 'Acente Başarıyla Guncellendi')
            return redirect("insurance:acente-listesi")
        else:
            messages.warning(request, 'Formu kontrol ediniz.')

    return render(request, 'Acente/acente-ekle.html', {'form': form, 'form_acente': form_acente})
