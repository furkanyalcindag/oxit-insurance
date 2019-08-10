from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from accounts.forms import LoginForm
from django.contrib import auth, messages
from django.urls import reverse





# Create your views here.


def index(request):
    return render(request, 'accounts/index.html')


# def login(request):
# return render(request, 'registration/login.html')


def login(request):

    if request.user.is_authenticated is True:
        if request.user.groups.all()[0].name == "Acente":
            return redirect('insurance:trafik-acente-policelerim')
        else:

            return redirect('insurance:acente-policeleri')


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            #return render(request, 'patient/:patient/index', context={})
            if user.groups.all()[0].name == "Acente":
                return redirect('insurance:trafik-acente-policelerim')
            else:

                return redirect('insurance:acente-policeleri')

        else:
            messages.add_message(request, messages.SUCCESS, 'Kullanıcı adı veya şifre hatalı')
            return render(request, 'registration/login.html')

    return render(request, 'registration/login.html')




