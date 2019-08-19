from django.conf.urls import url

from insurance.views import AcenteViews, SigortaSirketViews, AyarViews, ZeyilViews
from insurance.views.AnaAcenteViews import AnaAcenteViews, KaskoAnaAcenteViews
from insurance.views.Teklif import TrafikTeklifViews, KaskoTeklifViews

app_name = 'insurance'

urlpatterns = [

    url(r'acente-ekle/$', AcenteViews.acente_ekle, name='acente-ekle'),
    url(r'acente-listesi/$', AcenteViews.acente_list, name='acente-listesi'),
    url(r'^acente-duzenle/(?P<pk>\d+)$', AcenteViews.acente_guncelle, name='acente-duzenle'),

    url(r'sirket-ekle/$', SigortaSirketViews.sirket_ekle, name='sirket-ekle'),
    url(r'sirket-listesi/$', SigortaSirketViews.sirket_liste, name='sirket-listesi'),
    url(r'^sirket-duzenle/(?P<pk>\d+)$', SigortaSirketViews.sirke_guncelle, name='sirket-duzenle'),

    url(r'ayar-listesi/$', AyarViews.ayar_liste, name='ayar-listesi'),

    # Acente
    url(r'acente_musteriler/$', AcenteViews.acente_musterileri, name='acente-musterileri'),

    # trafik
    url(r'trafik-teklif-iste/$', TrafikTeklifViews.teklif_olustur_trafik, name='trafik-teklif-iste'),
    url(r'trafik-teklif-talepleri/$', TrafikTeklifViews.teklif_taleplerim, name='trafik-teklif-talepleri'),
    url(r'^trafik-teklif-cevapla/(?P<pk>\d+)$', TrafikTeklifViews.teklif_cevapla, name='trafik-teklif-cevapla'),
    url(r'^trafik-acente-policelerim/$', TrafikTeklifViews.acente_policeleri,
        name='trafik-acente-policelerim'),
    url(r'^acente-istatistik/$', TrafikTeklifViews.acente_policeleri,
        name='acente-istatistik'),

    url(r'^odemelerim/$', TrafikTeklifViews.acente_policeleri,
        name='odemelerim'),

    # anaacente trafik

    url(r'bekleyen-trafik-teklif/$', AnaAcenteViews.bekleyen_talepler, name='bekleyen-trafik-istek'),
    url(r'cevaplanan-trafik-teklif/$', AnaAcenteViews.cevaplanan_talepler, name='cevaplanan-trafik-istek'),
    url(r'^trafik-teklif-olustur/(?P<pk>\d+)$', AnaAcenteViews.trafikTeklifVer, name='trafik-olustur'),
    url(r'^trafik-teklif-incele/(?P<pk>\d+)$', AnaAcenteViews.trafikTeklifIncele, name='trafik-incele'),
    url(r'^trafik-police-olustur/(?P<pk>\d+)$', AnaAcenteViews.trafik_police_olustur, name='trafik-policesi-olustur'),

    url(r'^trafik-acente-policeleri/$', AnaAcenteViews.acente_policeleri, name='acente-policeleri'),

    # kasko
    url(r'kasko-teklif-iste/$', KaskoTeklifViews.teklif_olustur_kasko, name='kasko-teklif-iste'),
    url(r'kasko-teklif-talepleri/$', KaskoTeklifViews.kasko_teklif_taleplerim, name='kasko-teklif-talepleri'),
    url(r'^kasko-teklif-cevapla/(?P<pk>\d+)$', KaskoTeklifViews.teklif_cevapla, name='kasko-teklif-cevapla'),
    url(r'^kasko-acente-policelerim/$', KaskoTeklifViews.acente_kasko_policeleri,
        name='kasko-acente-policelerim'),

    # anaacente kasko

    url(r'bekleyen-kasko-teklif/$', KaskoAnaAcenteViews.kasko_bekleyen_talepler, name='bekleyen-kasko-istek'),
    url(r'cevaplanan-kasko-teklif/$', KaskoAnaAcenteViews.kasko_cevaplanan_talepler, name='cevaplanan-kasko-istek'),
    url(r'^kasko-teklif-olustur/(?P<pk>\d+)$', KaskoAnaAcenteViews.KaskoTeklifVer, name='kasko-olustur'),
    url(r'^kasko-teklif-incele/(?P<pk>\d+)$', KaskoAnaAcenteViews.kaskoTeklifIncele, name='kasko-incele'),
    url(r'^kasko-police-olustur/(?P<pk>\d+)$', KaskoAnaAcenteViews.kasko_police_olustur, name='kasko-police-olustur'),

    url(r'^kasko-acente-policeleri/$', KaskoAnaAcenteViews.acente_policeleri, name='kasko-acente-policeleri'),



    #Acente Zeyil

    url(r'zeyil-talebi-olustur/$', ZeyilViews.zeyil_olustur, name='zeyil-talebi-olustur'),
    url(r'acente-zeyil-talepleri/$', ZeyilViews.zeyil_taleplerim, name='acente-zeyil-talepleri'),

    # AnaAcente Zeyil

    url(r'zeyil-talebi-durum-guncelle/(?P<pk>\d+)$', ZeyilViews.zeyil_durum_guncelle, name='zeyil-durum-guncelle'),
    url(r'zeyil-talepleri/$', ZeyilViews.zeyil_talepleri_tum, name='zeyil-istekleri'),

]
