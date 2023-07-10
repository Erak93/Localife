from django.contrib import admin
from django.urls import path , include
from search_app import views

from django.urls import path
from .views import ExperienceSearchView,search_app_result

app_name="search_app"

urlpatterns = [
    path('experiences/search/', ExperienceSearchView.as_view(), name='experience_search'),
    path('experiences/search/results', search_app_result, name='experience_search_results'),
]