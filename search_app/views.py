from django.shortcuts import render,get_object_or_404

# Create your views here.
from user_app.models import Experience
from .filters import ExperienceFilter, SecondFilter, APIFilter
from .serializers import ExperienceSerializer, APISerializer

from django.views.generic import ListView
from django.db.models import Q



def search_app_result(request):
    return render(request,'search_app/experience_search_results.html')

def experience_details(request,experience_id):
    # Fetch the experience object or handle the case when it doesn't exist
    experience = get_object_or_404(Experience, id=experience_id)

    context = {
        'experience': experience,
        'experience_id':experience_id

    }
    return render(request, 'search_app/experience_details.html', context)

def host_profile(request,experience_id):
    # Fetch the experience object or handle the case when it doesn't exist
    experience = get_object_or_404(Experience, id=experience_id)
    all_experiences = Experience.objects.all()

    context = {
        'experience': experience,
        'experience_id':experience_id,
        'all_experiences': all_experiences,
    }
    return render(request, 'search_app/host_profile.html', context)


''' KAI'S PART'''

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

