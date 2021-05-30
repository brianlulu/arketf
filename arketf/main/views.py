from django.shortcuts import render
from django.http import HttpResponse
from .models import Stock, Trade


def home(request):

    return render(request, 'main/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'main/about.html', {'title': 'About'})


def dailytrade(request):
    
    trades = {
        'trades': Trade.objects.all()
    }

    return render(request, 'main/dailytrade.html', trades, {'title': 'DailyTrade'})
