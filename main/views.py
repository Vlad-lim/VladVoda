from typing import List
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import ElectronForm, InternetForm, OnlineForm, LoginForm, RegistrationForm, AppoitmentForm, IndicationForm, ActiveForm
from .models import Vakansies, Graphic, News, DonTarif, AsinTarif, ZugTarif, NotarialDocs, Con
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView
# Create your views here.


class NewsDetail(DetailView):
    model = News
    template_name = 'main/news-detail.html'
    context_object_name = 'new'


def allNews_view(request):
    new = News.objects.all()
    data = {
        'news':new
    }
    return render(request, 'main/AllNews.html', data)

    

def electron_view(request):
    status = ''
    if request.method == 'POST':
        form = ElectronForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            status = 'Успешно'
        else:
            status = 'Произошла ошибка, данные некоректно заполненны'
    form = ElectronForm()
    data = {
        'form': form,
        'status': status
    }
    return render(request, 'main/electronaya-priyomnaya.html', data)

def online_view(request):
    status = ''
    if request.method == 'POST':
        form = OnlineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            status = 'Успешно'
        else:
            status = 'Произошла ошибка, данные некоректно заполненны'
    form = OnlineForm()
    data = {
        'form': form,
        'status': status
    }
    return render(request, 'main/online-zayavka.html', data)



def cabinet_view(request):
    return render(request, 'main/Personal_cabinet.html')

def don_view(request):
    return render(request, 'main/don.html')

def zug_view(request):
    return render(request, 'main/zug.html')

def asin_view(request):
    return render(request, 'main/asin.html')
    

def indications_view(request):
    status = ''
    if request.method == 'POST':
        form = IndicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            status = 'Успешно'
            return redirect('/')
        else:
            status = 'Произошла ошибка, данные некоректно заполненны'
    form = IndicationForm()
    data = {
        'form': form,
        'status': status
    }
    return render(request, 'main/indications.html', data)



def index(request):
    new = News.objects.order_by('-id')[0:4]
    data = {
        'news':new
    }
    return render(request, 'main/index.html', data)


def activeHuman_view(request):
    status = ''
    if request.method == 'POST':
        form = ActiveForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            status = 'Успешно'
            return redirect('/')
        else:
            status = 'Произошла ошибка, данные некоректно заполненны'
    form = ActiveForm()
    data = {
        'form': form,
        'status': status
    }
    return render(request, 'main/ActiveHuman.html', data)


def faq_view(request):
    return render(request, 'main/faq.html')


def doc_view(request):
    model = NotarialDocs.objects.all()
    data = {
        'model': model
    }
    return render(request, 'main/docs.html', data)


def contact_view(request):
    model = Con.objects.all()
    data = {
        'Con':model
    }
    return render(request, 'main/contacts.html', data)


def abonent_view(request):
    return render(request, 'main/abonent.html')


def vakansies_view(request):
    model = Vakansies.objects.all()
    data = {
        'model': model
    }
    return render(request, 'main/vakansies.html', data)


def graphic_view(request):
    model = Graphic.objects.all()
    data = {
        'model': model,
    }
    return render(request, 'main/graphic.html', data)


def appoitment_view(request):
    status = ''
    if request.method == 'POST':
        form = AppoitmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            status = 'Успешно'
        else:
            status = 'Произошла ошибка, данные некоректно заполненны'
    form = AppoitmentForm()
    data = {
        'form': form,
        'status': status
    }
    
    return render(request, 'main/appoitment.html', data)

def tarrifs_view(request):
    DonModel = DonTarif.objects.all()
    ZugModel = ZugTarif.objects.all()
    AsinModel = AsinTarif.objects.all()
    data = {
        'Asin':AsinModel,
        'Zug':ZugModel,
        'Don': DonModel
    }
    return render(request, 'main/tarrifs.html', data)

def internet_view(request):
    status = ''
    form = InternetForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = InternetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            status = 'Успешно'
        else:
            status = 'Произошла ошибка'

    data = {
        'status':status,
        'form':form
    }
    return render(request, 'main/internet.html', data)




def LoginView(request):
    Error = ''
    succses = ''
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                succses = 'Успешно'
                return redirect('/cab')
            else:
                Error = 'Ошибка'
        else:
            Error = 'Ошибка'




    form = LoginForm(request.POST)
    context = {
        'form':form,
        'succses':succses,
        'Error':Error
    }
    return render(request, 'main/SignIn.html', context)

def RegistrationView(request):
    status = ''
    form = RegistrationForm(request.POST)
    context = {
        'status':status,
        'form':form,
    }
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.username = form.cleaned_data['username']
        new_user.email = form.cleaned_data['email']
        new_user.first_name = form.cleaned_data['first_name']
        new_user.last_name = form.cleaned_data['last_name']
        
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        return redirect('/SignIn')
        #username = form.cleaned_data['username']
        #password = form.cleaned_data['password']
        #user = authenticate(username=new_user.username, password=new_user.set_password())
        #if user:
           # login(request, user)
    else:
        status = 'Произошла ошибка, проверьте правильно ли вы заполнили все данные'

        

    return render(request, 'main/Registration.html', context )

def Logout_view(request):
    logout(request)
    return redirect('/')

class SearchResultsView(ListView):
    model = News
    template_name = 'main/Search-results.html'
 
    def get_queryset(self): 
        query = self.request.GET.get('q')
        
        object_list = News.objects.filter(
            Q(Tittle__icontains=query) | Q(Published__icontains=query)
        )
        return object_list

class DateSearchResult(ListView):
    model = News
    template_name = 'main/DateSearchResult.html'
    def get_queryset(self): 
        query = self.request.GET.get('d')
        object_list = News.objects.filter(
            Q(Published__icontains=query)
        )
        return object_list

def planningWork_view(request):
    return render(request, 'main/planningWork.html')

def WaterQa_view(request):
    return render(request, 'main/WaterQa.html')


def Dolg_view(request):
    return render(request, 'main/Dolg.html')