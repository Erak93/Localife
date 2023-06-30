from django.shortcuts import render
from .models import Continent, Offer

from django.shortcuts import render
from .models import Continent, Offer

def world_map(request):
    continents = Continent.objects.all()
    offers = Offer.objects.all()
    context = {
        'continents': continents,
        'offers': offers
    }
    return render(request, 'search_app/worldmap.html', context)


def continent_offers(request, continent_id):
    continent = Continent.objects.get(id=continent_id)
    offers = Offer.objects.filter(country__continent=continent)
    return render(request, 'continent_offers.html', {'continent': continent, 'offers': offers})


def index(request):
    return render(request, "search_app/base.html")