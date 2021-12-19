from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import SearchResultsView

urlpatterns = [
    path('', views.index),
    path('cab', views.cabinet_view, name = 'cab'),
    path('indications', views.indications_view, name='indications'),
    path('ActiveHuamn', views.activeHuman_view, name='activehuman'),
    path('Faq', views.faq_view, name='faq'),
    path('Documents', views.doc_view, name='doc'),
    path('Contacts', views.contact_view, name='contact'),
    path('Abonent', views.abonent_view, name='abon'),
    path('Vakansies', views.vakansies_view, name='vak'),
    path('Graphic', views.graphic_view, name='graph'),
    path('appoitment', views.appoitment_view, name='appoit'),
    path('news/<int:pk>', views.NewsDetail.as_view(), name = 'detail'),
    path('tarrifs', views.tarrifs_view, name = 'tarr'),
    path('internet_priemnaya', views.internet_view, name = 'inter'),
    path('don', views.don_view, name = 'don'),
    path('zug', views.zug_view, name = 'zug'),
    path('asin', views.asin_view, name = 'asin'),
    path('onlineZayavka', views.online_view, name = 'online'),
    path('electronayaPriyomnaya', views.electron_view, name = 'electron'),
    path('SignIn', views.LoginView, name='login'),
    path('Registration', views.RegistrationView, name='registration'),
    path('allNews', views.allNews_view, name = 'news'),
    path('LogOut', views.Logout_view, name='LogOut'),
    path('Search', SearchResultsView.as_view(), name='search_results'),
    path('planningWork', views.planningWork_view, name = 'plan'),
    path('DateSearchResult', views.DateSearchResult.as_view(), name = 'date'),
    path('WaterQa', views.WaterQa_view, name = 'water'),
    path('Dolg', views.Dolg_view, name = 'dolg'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
