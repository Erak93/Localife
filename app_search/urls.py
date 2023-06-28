from django.contrib import admin
from django.urls import path , include
from app_search import views

from django.urls import path
from .views import ExperienceSearchView

urlpatterns = [
    path('experiences/search/', ExperienceSearchView.as_view(), name='experience_search'),
]
