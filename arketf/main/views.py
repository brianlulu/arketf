from django.shortcuts import render
from django.http import HttpResponse
from .models import Stock

stocks = [
    {
        'name': 'Tesla',
        'ticker': 'TSLA',
        'price': 100.87,
        'market_cap': 98.87,
    },
        {
        'name': 'Microsoft',
        'ticker': 'MSFT',
        'price': 187.87,
        'market_cap': 870.87,
    },
]

fund = [
    {
        'name': 'ARKK',
        'holdings': ['Tesla', 'Microsoft']
    }
]

def home(request):

    return render(request, 'main/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'main/about.html', {'title': 'About'})


def dailytrade(request):
    
    holding = {
        'stocks': Stock.objects.all()
    }

    return render(request, 'main/dailytrade.html', holding, {'title': 'DailyTrade'})
