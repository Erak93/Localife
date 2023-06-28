from django.contrib import admin
from django.urls import path , include
from app_user import views


app_name="user_app"

urlpatterns = [
   
    path("",views.user_app, name="user_app"),  #This is shown when we go to www...../user
  
]