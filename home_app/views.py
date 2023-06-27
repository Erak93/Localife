from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

app_name="home_app"

def home_app(request):
    return render(request,'home_app/home_app.html')
