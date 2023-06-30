from django.contrib.gis.db import models
from django_countries.fields import CountryField

class Continent(models.Model):
    name = models.CharField(max_length=50)
    mpoly = models.MultiPolygonField()

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    mpoly = models.MultiPolygonField()

    def __str__(self):
        return self.name

class Offer(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    # Other fields for the offer

    def __str__(self):
        return self.name
