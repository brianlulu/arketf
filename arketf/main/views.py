from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):

    return render(request, 'main/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'main/about.html', {'title': 'About'})


def dailytrade(request):
    
    trades = {
        'trades': Trade.objects.all()
    }

    return render(request, 'main/dailytrade/dailytrade.html', trades, {'title': 'DailyTrade'})

def arkk(request):
    
    fund = Fund.objects.get(ticker = 'ARKK')

    trades = {
        'trades': Trade.objects.filter(fund = fund)
    }

    return render(request, 'main/dailytrade/arkk.html', trades, {'title': 'ARKK-DailyTrade'})


def arkq(request):
    
    fund = Fund.objects.get(ticker = 'ARKQ')

    trades = {
        'trades': Trade.objects.filter(fund = fund)
    }

    return render(request, 'main/dailytrade/arkq.html', trades, {'title': 'ARKQ-DailyTrade'})


def arkf(request):
    
    fund = Fund.objects.get(ticker = 'ARKF')

    trades = {
        'trades': Trade.objects.filter(fund = fund)
    }

    return render(request, 'main/dailytrade/arkf.html', trades, {'title': 'ARKF-DailyTrade'})


def arkg(request):
    
    fund = Fund.objects.get(ticker = 'ARKG')

    trades = {
        'trades': Trade.objects.filter(fund = fund)
    }

    return render(request, 'main/dailytrade/arkg.html', trades, {'title': 'ARKG-DailyTrade'})


def arkw(request):
    
    fund = Fund.objects.get(ticker = 'ARKW')

    trades = {
        'trades': Trade.objects.filter(fund = fund)
    }

    return render(request, 'main/dailytrade/arkw.html', trades, {'title': 'ARKW-DailyTrade'})


def arkx(request):
    
    fund = Fund.objects.get(ticker = 'ARKX')

    trades = {
        'trades': Trade.objects.filter(fund = fund)
    }

    return render(request, 'main/dailytrade/arkx.html', trades, {'title': 'ARKX-DailyTrade'})


def prnt(request):
    
    fund = Fund.objects.get(ticker = 'PRNT')

    trades = {
        'trades': Trade.objects.filter(fund = fund)
    }

    return render(request, 'main/dailytrade/prnt.html', trades, {'title': 'PRNT-DailyTrade'})

def izrl(request):
    
    fund = Fund.objects.get(ticker = 'IZRL')

    trades = {
        'trades': Trade.objects.filter(fund = fund)
    }

    return render(request, 'main/dailytrade/izrl.html', trades, {'title': 'IZRL-DailyTrade'})

