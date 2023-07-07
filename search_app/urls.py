from django.urls import path, include
from rest_framework import routers
from .views import index, SearchAPIView

router = routers.DefaultRouter()
router.register(r'',SearchAPIView)

app_name = "search_app"
urlpatterns = [
    # Other URLs in your project
    path("", index, name="search_index"),
    #path('api/', SearchAPIView.as_view()),
    path('api/', include(router.urls), name='search_api')
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

