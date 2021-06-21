from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'main-home'),
    path('about/', views.about, name = 'main-about'),
    path('dailytrade/', views.dailytrade, name = 'main-dailytrade'),
    path('dailytrade/arkk/', views.arkk, name = 'main-dailytrade-arkk'),
    path('dailytrade/arkq/', views.arkq, name = 'main-dailytrade-arkq'),
    path('dailytrade/arkf/', views.arkf, name = 'main-dailytrade-arkf'),
    path('dailytrade/arkg/', views.arkg, name = 'main-dailytrade-arkg'),
    path('dailytrade/arkw/', views.arkw, name = 'main-dailytrade-arkw'),
    path('dailytrade/arkx/', views.arkx, name = 'main-dailytrade-arkx'),
    path('dailytrade/prnt/', views.prnt, name = 'main-dailytrade-prnt'),
    path('dailytrade/izrl/', views.izrl, name = 'main-dailytrade-izrl'),
]
