from django.contrib import admin
from django.urls import path , include
from search_app import views

urlpatterns = [
   
    path("",views.search_app, name="search_app"),
  
]