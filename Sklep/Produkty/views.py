from django.shortcuts import render
from django.http import HttpResponse
from .models import Produkt, Producent, Kategoria

def index(request):
    kategorie = Kategoria.objects.all()

    context = {'kategorie' : kategorie}
    return render(request, 'Produkty/index.html', context)

def kategoria(request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    kategoria_produkt = Produkt.objects.filter(kategoria=kategoria_user)
    kategorie = Kategoria.objects.all()
    context = {'kategoria_user' : kategoria_user,
               'kategoria_produkt' : kategoria_produkt,
               'kategorie' : kategorie}
    return render(request, 'Produkty/kategoria_produkt.html', context)

def produkt(request, id):
    kategorie = Kategoria.objects.all()
    produkt_user = Produkt.objects.get(pk=id)
    context = {'produkt_user' : produkt_user,
               'kategorie' : kategorie}
    return render(request, 'Produkty/produkt.html', context)