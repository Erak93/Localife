from django.contrib import admin
from django.urls import path , include
from app_search import views


app_name="search_app"

urlpatterns = [
   
    path("",views.search_app, name="search_app"),
  
]