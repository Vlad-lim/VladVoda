from django.shortcuts import render
from .models import Rucovodstvo

# Create your views here.


def about(request):
    return render(request, 'about/About.html')


def history(request):
    return render(request, 'about/History.html')


def structure(request):
    return render(request, 'about/Structure.html')


def rucovodstvo(request):
    admins = Rucovodstvo.objects.all()
    data = {
        'admins': admins
    }
    return render(request, 'about/Rucovodstvo.html', data)


def info(request):
    return render(request, 'about/Info.html')


def finance(request):
    return render(request, 'about/Finance.html')


def eco(request):
    return render(request, 'about/Eco.html')
