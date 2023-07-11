 

from django.urls import path
from .views import search_app_result,experience_details

# # router = routers.DefaultRouter()
# # router.register('experiences', ExperienceViewSet)

urlpatterns = [
    #path('experiences/search/', ExperienceSearchView.as_view(), name='experience_search'),
    path('experiences/search/results', search_app_result, name='experience_search_results'),
    path('experiences/search/results/details/<int:experience_id>/', experience_details, name='experience_details'),
]
