from rest_framework.response import Response
from rest_framework.decorators import api_view
from user_app.models import Experience
from .serializers import ExperienceSerializer

@api_view(['GET']) # here we can put all the allowed methods which are get, post, put and delete
def getData(request):
    items=Experience.objects.all()
    serializer=ExperienceSerializer(items, many="True") # here we serialize all the objects in Items
    return Response(serializer.data) # this will be outputed as JSON data


@api_view(['POST'])
def addItem(request):
    serializer=ExperienceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer)