from django.contrib import admin
from django.urls import path
from post_app import views

app_name="post_app"

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('detail/', views.post_detail, name='post_detail'),
    path('update/', views.post_list, name='post_update'),
    path('delete/', views.post_list, name='post_delete'),
    path('like/', views.post_list, name='post_like'),
    path('unlike/', views.post_list, name='post_unlike'),
    path('list/', views.post_list, name='post_list'),
]