from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
import json



def home(request):

    labels = []
    data = []
    remain_holding_weight = 0.0
    remain_holding_label = "Other"

    arkk_obj = Fund.objects.get(ticker = 'ARKK')

    holdings = Holding.objects.filter(fund = arkk_obj).order_by('-weight')[:10]
    remain_holding = Holding.objects.filter(fund = arkk_obj).order_by('-weight')[10:]

    for h in holdings:
        labels.append(h.stock.ticker)
        data.append(float(h.weight))


    for r in remain_holding:
        remain_holding_weight += float(r.weight)
    
    data.append(remain_holding_weight)
    labels.append(remain_holding_label)

    return render(
        request, 
        'main/home.html', 
        {
            'title': 'Home',
            'labels': json.dumps(labels),
            'data': json.dumps(data),
        }
    )

def about(request):
    return render(request, 'main/about.html', {'title': 'About'})


def dailytrade(request):

    
    trades = Trade.objects.all().order_by('-date')
    
    paginator = Paginator(trades, 30)
    
    page = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(page.num_pages)

    return render(request,
        'main/dailytrade/dailytrade.html', 
        {
            'Title': 'DailyTrade',
            'page_obj':page_obj
        }
    )

def arkk(request):
    
    fund = Fund.objects.get(ticker = 'ARKK')

    trades = Trade.objects.filter(fund = fund).order_by('-date')

    paginator = Paginator(trades, 30)
    
    page = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(page.num_pages)

    return render(request, 'main/dailytrade/arkk.html', {'title': 'ARKK-DailyTrade', 'page_obj': page_obj})


def arkq(request):
    
    fund = Fund.objects.get(ticker = 'ARKQ')
    
    trades = Trade.objects.filter(fund = fund).order_by('-date')

    paginator = Paginator(trades, 30)
    
    page = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(page.num_pages)    

    return render(request, 'main/dailytrade/arkq.html', {'title': 'ARKQ-DailyTrade', 'page_obj': page_obj})


def arkf(request):
    
    fund = Fund.objects.get(ticker = 'ARKF')
    trades = Trade.objects.filter(fund = fund).order_by('-date')
    paginator = Paginator(trades, 30)
    
    page = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(page.num_pages) 

    return render(request, 'main/dailytrade/arkf.html', {'title': 'ARKF-DailyTrade', 'page_obj': page_obj})


def arkg(request):
    
    fund = Fund.objects.get(ticker = 'ARKG')
    
    trades = Trade.objects.filter(fund = fund).order_by('-date')
    paginator = Paginator(trades, 30)
    
    page = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(page.num_pages) 

    return render(request, 'main/dailytrade/arkg.html', {'title': 'ARKG-DailyTrade', 'page_obj': page_obj})


def arkw(request):
    
    fund = Fund.objects.get(ticker = 'ARKW')
    
    trades = Trade.objects.filter(fund = fund).order_by('-date')
    paginator = Paginator(trades, 30)
    
    page = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(page.num_pages) 

    return render(request, 'main/dailytrade/arkw.html', {'title': 'ARKW-DailyTrade', 'page_obj': page_obj})


def arkx(request):
    
    fund = Fund.objects.get(ticker = 'ARKX')

    trades = Trade.objects.filter(fund = fund).order_by('-date')
    paginator = Paginator(trades, 30)
    
    page = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(page.num_pages) 

    return render(request, 'main/dailytrade/arkx.html', {'title': 'ARKX-DailyTrade', 'page_obj': page_obj})


def prnt(request):
    
    fund = Fund.objects.get(ticker = 'PRNT')
    
    trades = Trade.objects.filter(fund = fund).order_by('-date')
    paginator = Paginator(trades, 30)
    
    page = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(page.num_pages) 

    return render(request, 'main/dailytrade/prnt.html', {'title': 'PRNT-DailyTrade', 'page_obj': page_obj})

def izrl(request):
    
    fund = Fund.objects.get(ticker = 'IZRL')

    trades = Trade.objects.filter(fund = fund).order_by('-date')
    paginator = Paginator(trades, 30)
    
    page = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(page.num_pages) 

    return render(request, 'main/dailytrade/izrl.html', {'title': 'IZRL-DailyTrade', 'page_obj': page_obj})

