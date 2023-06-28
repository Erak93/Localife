from django.contrib import admin
from django.urls import path , include
from finished_app import views

app_name="finished_app"

urlpatterns = [
   
    path("",views.finished_app, name="finished_app"),
  
]
