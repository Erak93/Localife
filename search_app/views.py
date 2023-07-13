from django.shortcuts import render
from user_app.models import Experience
from .filters import ExperienceFilter, SecondFilter, APIFilter
from .serializers import ExperienceSerializer, APISerializer
# Create your views here

def index(request):
    filter1 = ExperienceFilter(request.GET, queryset=Experience.objects.all())
    queryset = filter1.qs

    filter2 = SecondFilter(request.GET, queryset=queryset)
    #queryset2 = filter2.qs

    context = {
        'filter1': filter1,
        'filter2': filter2,
    }
    return render(request, 'search_app/search_app.html', context)
"""
def granular(request, f):
    f2 = SecondFilter(request.GET, queryset=f)

    return render(request, 'search_app/granular_search.html', {"filter2": f2})
"""

from rest_framework import viewsets
from rest_framework.response import Response
from django_filters import rest_framework as drfilters

class SearchAPIView(viewsets.ModelViewSet):
        queryset = Experience.objects.all().order_by('region')
        serializer_class = APISerializer
        lookup_field = 'region'
        #filter_backends =(drfilters.DjangoFilterBackend, )
        #filterset_class = APIFilter
        #filterset_fields = ['price', 'start_date', 'end_date', 'region__region_name', 'host__username', 'experience_tags__tag_name']
        #filter_instance = APIFilter(request.query_params, queryset=queryset)
        #queryset = filter_instance.qs

        #serializer = ExperienceSerializer(queryset, many=True)

        def filter_queryset(self, queryset):
              filter_backends = (drfilters.DjangoFilterBackend, )
              
              for backend in list(filter_backends):
                    queryset = backend().filter_queryset(self.request, queryset, view=self)
              return queryset
        filterset_class = APIFilter

