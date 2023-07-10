from django.contrib import admin
from django.urls import path , include
from user_app import views
from django.contrib.auth import views as auth_views


app_name="user_app"

urlpatterns = [
    path("index/", views.index , name="index"),
    path("register/",views.register, name="register"),  
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("registration_success/", views.registration_success, name="success"),
    path("profile/",views.profile, name="user_profile")
]