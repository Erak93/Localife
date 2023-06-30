from django.urls import path
from search_app import views

app_name = 'search_app'

urlpatterns = [
    path("", views.index, name='index'  ),
    path('worldmap/', views.world_map, name='world_map'),
    # other URL patterns...
]
