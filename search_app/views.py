from django.shortcuts import render

# Create your views here.
from user_app.models import Experience

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

