from django.conf.urls import url

from insurance.views import AcenteViews, SigortaSirketViews, AyarViews

app_name = 'insurance'

urlpatterns = [

    url(r'acente-ekle/$', AcenteViews.acente_ekle, name='acente-ekle'),
    url(r'acente-listesi/$', AcenteViews.acente_list, name='acente-listesi'),
    url(r'^acente-duzenle/(?P<pk>\d+)$', AcenteViews.acente_guncelle, name='acente-duzenle'),

    url(r'sirket-ekle/$', SigortaSirketViews.sirket_ekle, name='sirket-ekle'),
    url(r'sirket-listesi/$', SigortaSirketViews.sirket_liste, name='sirket-listesi'),
    url(r'^sirket-duzenle/(?P<pk>\d+)$', SigortaSirketViews.sirke_guncelle, name='sirket-duzenle'),

    url(r'ayar-listesi/$', AyarViews.ayar_liste, name='ayar-listesi'),

]
