from django.shortcuts import render
from django.http import HttpResponse
from .models import Produkt, Producent, Kategoria

def index(request):
    kategorie = Kategoria.objects.all()

    context = {'kategorie' : kategorie}
    return render(request, 'Produkty/index.html', context)

def kategoria(request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    return HttpResponse(kategoria_user)

def produkt(request, id):
    produkt_user = Produkt.objects.get(pk=id)
    napis = "<h1>" + str(produkt_user) + "</h1>" + \
            "<p>" + str(produkt_user.opis) + "</p>" + \
            "<p>" + str(produkt_user.cena) + "</p>"
    return HttpResponse(napis)