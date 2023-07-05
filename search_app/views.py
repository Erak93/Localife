from django.shortcuts import render
from user_app.models import Experience
from .filters import ExperienceFilter, SecondFilter
# Create your views here

def index(request):
    filter1 = ExperienceFilter(request.GET, queryset=Experience.objects.all())
    queryset = filter1.qs

    filter2 = SecondFilter(request.GET, queryset=queryset)
    queryset2 = filter2.qs

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
