from django.contrib import admin
from django.urls import path , include
from user_app import views

urlpatterns = [
   
<<<<<<< HEAD
    path("",views.user_app, name="user_app"),  #This is shown when we go to www...../user
=======
    path("",views.user_app, name="user_app"),  #This is shown when we go to www.../user
>>>>>>> origin/Pepper
  
]