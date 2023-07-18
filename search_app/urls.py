from django.contrib import admin
from django.urls import path , include

from .views import index, SearchAPIView
from rest_framework import routers



from .views import search_app_result,experience_details,host_profile

app_name="search_app"


router = routers.DefaultRouter()
router.register(r'api',SearchAPIView, basename='api')


urlpatterns = [
    path("", index, name="search_index"),
    path(r'', include(router.urls)),
    path('experiences/search/results', search_app_result, name='experience_search_results'),
    path('experiences/search/results/details/<int:experience_id>/host', host_profile, name='host_profile'),
    path('experiences/search/results/details/<int:experience_id>/', experience_details, name='experience_details'),
    
    
]
