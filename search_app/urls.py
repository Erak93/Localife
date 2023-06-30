from django.urls import path, include
from rest_framework import routers
from .views import ExperienceViewSet

<<<<<<< HEAD
router = routers.DefaultRouter()
router.register('experiences', ExperienceViewSet)

urlpatterns = [
    # Other URLs in your project
    path('api/', include(router.urls)),
]

=======
from django.urls import path
from .views import ExperienceSearchView

urlpatterns = [
    path('experiences/search/', ExperienceSearchView.as_view(), name='experience_search'),
]
>>>>>>> aleksV2
