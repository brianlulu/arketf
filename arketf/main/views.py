from django.shortcuts import render
from django.http import HttpResponse

stocks = [
    {
        'name': 'Tesla',
        'ticker': 'TSLA',
        'price': 100.87
    },
        {
        'name': 'Microsoft',
        'ticker': 'MSFT',
        'price': 187.87
    },
]

fund = [
    {
        'name': 'ARKK',
        'holdings': ['Tesla', 'Microsoft']
    }
]

def home(request):
    
    holding = {
        'stocks': stocks 
    }

    return render(request, 'main/home.html', holding, {'title': 'Home'})

def about(request):
    return render(request, 'main/about.html', {'title': 'About'})
