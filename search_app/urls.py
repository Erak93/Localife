from django.urls import path
from .views import world_map

app_name = 'search_app'

urlpatterns = [
    path('worldmap/', world_map, name='world_map'),
    # other URL patterns...
]
