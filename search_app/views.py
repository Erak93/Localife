from django.shortcuts import render,get_object_or_404

# Create your views here.
from user_app.models import Experience,Review
from .filters import ExperienceFilter, SecondFilter, APIFilter
from .serializers import ExperienceSerializer, APISerializer

from django.views.generic import ListView
from django.db.models import Q
from .models import Booking
from django.http import HttpResponse




def search_app_result(request):
    return render(request,'search_app/experience_search_results.html')

def experience_details(request,experience_id):
    """
    OLD VERSION (WORKING)
    
    # Fetch the experience object or handle the case when it doesn't exist
    experience = get_object_or_404(Experience, id=experience_id)

    
    booking = Booking(
            traveler=request.user.user_profile,
            host=experience.host,
            experience_name=experience.title,
        )

    context = {
        'experience': experience,
        'experience_id':experience_id,
        'booking': booking,  # Pass the booking variable to the template

    }
    return render(request, 'search_app/experience_details.html', context)
"""

    
    if request.user.is_anonymous:
         return HttpResponse("No user")
    else:
        # Fetch the experience object or handle the case when it doesn't exist
        experience = get_object_or_404(Experience, id=experience_id)
        review_list=Review.objects.all()

        if request.method == "POST":
            # Get data from the form submission
            traveler_post= request.POST.get("traveler")
            host_post= request.POST.get("host")
            experience_name = request.POST.get("experience_name")


            #If a booking already exists, redirect to other template
            booking = Booking(
                traveler=traveler_post,
                host=host_post,
                experience_name=experience_name,
                )

                
            existing_booking=Booking.objects.filter(traveler=request.user.user_profile,host=experience.host,experience_name=experience.title)
            if existing_booking:
                return HttpResponse("Sorry. You have already booked this experience")
            else:  
                    
                    
                booking.save()
                # Redirect to a success page or display a success message
                return HttpResponse("Booking successful!")
        else:
            context = {
                    'experience': experience,
                    'experience_id': experience_id,
                    'review_list':review_list,
                    
                }
            return render(request, 'search_app/experience_details.html', context)
        



    
def host_profile(request,experience_id):
    # Fetch the experience object or handle the case when it doesn't exist
    experience = get_object_or_404(Experience, id=experience_id)
    all_experiences = Experience.objects.all()

    context = {
        'experience': experience,
        'experience_id':experience_id,
        'all_experiences': all_experiences,
    }
    return render(request, 'search_app/host_profile.html', context)


''' KAI'S PART'''

def index(request):
    filter1 = ExperienceFilter(request.GET, queryset=Experience.objects.all())
    queryset = filter1.qs

    filter2 = SecondFilter(request.GET, queryset=queryset)
    #queryset2 = filter2.qs
    
    user=request.user
    if user.id==None or user.id-1<=0:
         user.id=1
         context = {
                'filter1': filter1,
                'filter2': filter2,
                'user_id':user.id-1
            }
         return render(request, 'search_app/search_app.html', context)
    else:
         context = {
                'filter1': filter1,
                'filter2': filter2,
                'user_id':user.id-1
            }
         return render(request, 'search_app/search_app.html', context)


    
"""
def granular(request, f):
    f2 = SecondFilter(request.GET, queryset=f)

    return render(request, 'search_app/granular_search.html', {"filter2": f2})
"""

from rest_framework import viewsets
from rest_framework.response import Response
from django_filters import rest_framework as drfilters

class SearchAPIView(viewsets.ModelViewSet):
        queryset = Experience.objects.all().order_by('region')
        serializer_class = APISerializer
        lookup_field = 'region'
        #filter_backends =(drfilters.DjangoFilterBackend, )
        #filterset_class = APIFilter
        #filterset_fields = ['price', 'start_date', 'end_date', 'region__region_name', 'host__username', 'experience_tags__tag_name']
        #filter_instance = APIFilter(request.query_params, queryset=queryset)
        #queryset = filter_instance.qs

        #serializer = ExperienceSerializer(queryset, many=True)

        def filter_queryset(self, queryset):
              filter_backends = (drfilters.DjangoFilterBackend, )
              
              for backend in list(filter_backends):
                    queryset = backend().filter_queryset(self.request, queryset, view=self)
              return queryset
        filterset_class = APIFilter

