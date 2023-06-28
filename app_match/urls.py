from django.contrib import admin
from django.urls import path , include
from app_match import views

app_name="match_app"

urlpatterns = [
   
    path("",views.match_app, name="match_app"),
  
]