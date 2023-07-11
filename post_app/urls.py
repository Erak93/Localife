from django.contrib import admin
from django.urls import path
from . import views

app_name="post_app"

urlpatterns = [

    path('' , views.experience_list , name="post_list"),
    path('list/', views.experience_list, name='experience_list'),
    path('create/', views.create_experience, name='post_create'),
    path('test_view/', views.test_view, name='test_view'),
    path('detail/<int:id>/', views.experience_detail, name='post_detail'),
]