from django.shortcuts import render,get_object_or_404

# Create your views here.
from user_app.models import Experience

from django.views.generic import ListView
from django.db.models import Q



def search_app_result(request):
    return render(request,'search_app/experience_search_results.html')

def experience_details(request,experience_id):
    # Fetch the experience object or handle the case when it doesn't exist
    experience = get_object_or_404(Experience, id=experience_id)

    context = {
        'experience': experience,
    }
    return render(request, 'search_app/experience_details.html', context)


