from django.shortcuts import render

# Create your views here.

app_name="home_app"

def home_app(request):
    return render(request,'home_app/home_app.html')