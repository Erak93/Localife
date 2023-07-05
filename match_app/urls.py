from django.contrib import admin
from django.urls import path
from match_app import views

app_name="match_app"

urlpatterns = [
   
    path("",views.match_app, name="match_app"),
    path('book/booking_product/<int:experience_id>/', views.book_offer, name='book_offer'),
    path("booking_success", views.booking_success, name="booking_success"),
  
]