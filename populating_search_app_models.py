import os
import django
from django.contrib.gis.geos import GEOSGeometry

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'localife_project.settings')
django.setup()

from search_app.models import Continent, Country, Offer

def populate_models():
    # Create continents
    continents_data = [
        {'name': 'Africa', 'mpoly': '{"type":"MultiPolygon","coordinates":[[[[30,0],[31,10],[40,10],[45,0],[30,0]]]]}'},
        {'name': 'Asia', 'mpoly': '{"type":"MultiPolygon","coordinates":[[[[60,10],[70,0],[80,10],[75,20],[60,10]]]]}'},
        {'name': 'Europe', 'mpoly': '{"type":"MultiPolygon","coordinates":[[[[10,40],[20,40],[20,50],[10,50],[10,40]]]]}'},
        # Add more continents as needed
    ]
    
    for continent_data in continents_data:
        continent = Continent(name=continent_data['name'], mpoly=GEOSGeometry(continent_data['mpoly']))
        continent.save()

    # Rest of the code...

    # Create countries
    countries_data = [
        {'name': 'Nigeria', 'continent': 'Africa'},
        {'name': 'India', 'continent': 'Asia'},
        {'name': 'Germany', 'continent': 'Europe'},
        # Add more countries as needed
    ]
    
    for country_data in countries_data:
        continent = Continent.objects.get(name=country_data['continent'])
        country = Country.objects.create(name=country_data['name'], continent=continent)
        print(f"Country created: {country.name}")

    # Create offers
    offers_data = [
        {'title': 'Safari Adventure', 'description': 'Explore the wildlife of Africa', 'latitude': 0, 'longitude': 30, 'country': 'Nigeria'},
        {'title': 'Trekking in the Himalayas', 'description': 'Experience the breathtaking beauty of the Himalayas', 'latitude': 10, 'longitude': 70, 'country': 'India'},
        {'title': 'Historical Tour of Berlin', 'description': 'Discover the rich history of Berlin', 'latitude': 40, 'longitude': 20, 'country': 'Germany'},
        # Add more offers as needed
    ]

    for offer_data in offers_data:
        country = Country.objects.get(name=offer_data['country'])
        offer = Offer.objects.create(title=offer_data['title'], description=offer_data['description'],
                                     latitude=offer_data['latitude'], longitude=offer_data['longitude'], country=country)
        print(f"Offer created: {offer.title}")

if __name__ == '__main__':
    populate_models()
