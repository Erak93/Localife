from django.contrib import admin
from django.urls import path , include
from app_finished import views

app_name="app_finished"

urlpatterns = [
   
    path("",views.app_finished, name="app_finished"),
  
]
