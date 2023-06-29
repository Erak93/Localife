from django.shortcuts import render

# Create your views here.
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




