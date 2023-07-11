from django.contrib import admin
from django.urls import path
from . import views

app_name="post_app"
# this is for previous version
# urlpatterns = [
#     path('', views.post_list, name='post_list'),
#     path('create/', views.post_create, name='post_create'),
#     path('detail/', views.post_detail, name='post_detail'),
#     path('update/', views.post_list, name='post_update'),
#     path('delete/', views.post_list, name='post_delete'),
#     path('like/', views.post_list, name='post_like'),
#     path('unlike/', views.post_list, name='post_unlike'),
#     path('list/', views.post_list, name='post_list'),
#]
urlpatterns = [

    path('' , views.experience_list , name="post_list"),
    path('list/', views.experience_list, name='experience_list'),
    path('create/', views.create_experience, name='post_create'),
    path('test_view/', views.test_view, name='test_view'),
    path('detail/<int:id>/', views.experience_detail, name='post_detail'),
]
