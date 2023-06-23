from django.contrib import admin
from django.urls import path
from post_app import views

urlpatterns = [
   
    path("",views.post_app, name="post_app"),
  
]