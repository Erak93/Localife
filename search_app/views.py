from django.shortcuts import render

# Create your views here.
<<<<<<< HEAD
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.response import Response

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['host__region']
    search_fields = ['experience_tags__name']

    @action(detail=False, methods=['get'])
    def list_all_experiences(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    


#To search experiences in a specific region, you can make a GET request to /api/experiences/?host__region=<region_name>.
#To search experiences by tags, you can make a GET request to /api/experiences/?search=<tag_name>.
#To retrieve a list of all experiences, you can make a GET request to /api/experiences/list_all_experiences/.

=======
from user_app.models import Experience
>>>>>>> aleksV2

from django.views.generic import ListView
from django.db.models import Q

class ExperienceSearchView(ListView):
    model = Experience
    template_name = 'experience_search.html'
    context_object_name = 'experiences'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        regions = self.request.GET.getlist('regions')
        tags = self.request.GET.getlist('tags')

        # Filter by regions
        if regions:
            queryset = queryset.filter(host__region__in=regions)

        # Filter by tags
        if tags:
            queryset = queryset.filter(experience_tags__in=tags)

        return queryset

