from django.shortcuts import render

# Create your views here.



def home_app(request):
    return render(request,'home_app/home_app.html')