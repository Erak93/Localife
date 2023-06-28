from django.contrib import admin
from django.urls import path
from app_home import views

app_name="home_app"

urlpatterns = [
   
    path("",views.home_app, name="home_app"),
  
]