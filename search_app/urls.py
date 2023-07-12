from django.contrib import admin
from django.urls import path , include
from search_app import views

from django.urls import path
from .views import search_app_result,experience_details,host_profile

app_name="search_app"

urlpatterns = [
    #path('experiences/search/', ExperienceSearchView.as_view(), name='experience_search'),
    path('experiences/search/results', search_app_result, name='experience_search_results'),
    path('experiences/search/results/details/<int:experience_id>/host', host_profile, name='host_profile'),
    path('experiences/search/results/details/<int:experience_id>/', experience_details, name='experience_details'),
    
]
