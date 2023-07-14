from django.contrib import admin
from django.urls import path
from match_app.views import book_offer,booking_success,available_experiences,match_app

app_name="match_app"

urlpatterns = [
   
    path("",match_app, name="match_app"),
    path('booking_product/<int:experience_id>/', book_offer, name='book_offer'),
    path("booking_success", booking_success, name="booking_success"),
    path('experiences/', available_experiences, name='available_experiences'),
]