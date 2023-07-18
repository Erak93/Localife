from django.contrib import admin
from django.urls import path
from match_app.views import match_app

app_name="match_app"

urlpatterns = [
   
    path("",match_app, name="match_app"),
]