from django.urls import path, include
#from rest_framework import routers
from .views import index

#router = routers.DefaultRouter()
#router.register('experiences', ExperienceViewSet)

app_name = "search_app"
urlpatterns = [
    # Other URLs in your project
    path("index/", index, name="search_index"),
    #path("granular/", granular, name="granular_search" )
    #path('api/', include(router.urls)),
]

