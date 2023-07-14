
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from user_app.models import Experience
from .serializers import ExperienceSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ExperienceForm
from rest_framework.parsers import MultiPartParser, FormParser

def test_view(request):
    return render(request, 'post_app/test_view.html')

def create_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #image = request.FILES.get('experience_image')
            #image = Experience.objects.create(experience_image=image)
            #image.save()
            
            #return render(request, ('home_app/home_app.html'))
            return render(request, 'post_app/test_view.html')
        
    else:
        form = ExperienceForm()
    return render(request, 'post_app/post_create.html', {'form': form})




@api_view(['GET'])
def experience_list(request): #, format=None):
    if request.method == 'GET': # and request.user.is_authenticated:
        queryset = Experience.objects.all() #.filter(user=request.user)
        serializer = ExperienceSerializer(queryset, many=True) #, context={'request': request})
        return Response(serializer.data) #, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE']) 
def experience_detail(request, id):
    experience = get_object_or_404(Experience, pk=id)
    if request.method == 'GET':
        serializer = ExperienceSerializer(experience)
        return Response(serializer.data) 

    elif request.method == 'DELETE':
        experience.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ExperienceUpdate(generics.RetrieveUpdateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    #permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        # Exclude 'experience_image' from request data if it exists
        request_data = request.data.copy()
        request_data.pop('experience_image', None)

        serializer = self.get_serializer(instance, data=request_data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

