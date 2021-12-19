from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.about, name='About'),
    path('O_predpriyatii/Nasha_istorya', views.history, name='History'),
    path('O_predpriyatii/Structura_predpriyatia',
         views.structure, name='Structure'),
    path('O_predpriyatii/Rukovodstvo', views.rucovodstvo, name='Rucovodstvo'),
    path('O_predpriyatii/Rascritie_informacii', views.info, name='Info'),
    path('O_predpriyatii/Finansovaya_otchetnost', views.finance, name='Finance'),
    path('O_predpriyatii/Ecologichescaya_politica', views.eco, name='Eco')
]
