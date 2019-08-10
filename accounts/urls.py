#import patterns as patterns
from django.urls import path, re_path

from accounts.forms import LoginForm
from . import views


app_name = 'accounts'

urlpatterns = [
   #path('', views.index, name='index'),
   path('', views.login)

]

