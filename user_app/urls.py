from django.contrib import admin
from django.urls import path , include
from user_app import views


app_name="user_app"

urlpatterns = [
    path("index/", views.index , name="index"),
    path("register/",views.register, name="register"),  
    path("login/", views.user_login, name="login"),
]