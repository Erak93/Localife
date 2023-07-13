from django.urls import path, include
from rest_framework import routers
from .views import index, SearchAPIView
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'api',SearchAPIView, basename='api')

app_name = "search_app"
urlpatterns = [
    # Other URLs in your project
    path("", index, name="search_index"),
    #path('api/', SearchAPIView.as_view()),
    path(r'', include(router.urls))
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)

#import pprint
#pprint.pprint(router.get_urls())