from django.contrib import admin
from django.urls import path
from app_post import views

app_name="post_app"

urlpatterns = [
   
    path("",views.post_app, name="post_app"),
  
]