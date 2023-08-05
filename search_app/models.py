from django.db import models

# Create your models here.


from django.views.generic import ListView
from django.db.models import Q
from user_app.models import Experience
from user_app.models import UserProfile,Experience

class Booking(models.Model):
    
    traveler=models.CharField(max_length=50)
    host=models.CharField(max_length=50)
    experience_name=models.CharField(max_length=200)
    """
    traveler=models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    host=models.ForeignKey(UserProfile, on_delete=models.CASCADE ,related_name='host_bookings')
    experience_name=models.ForeignKey(Experience,on_delete=models.CASCADE, related_name='bookings')
    """
    
    def __str__(self):
        return f' traveler: {self.traveler} , host: {self.host} , experience: {self.experience_name}'


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
