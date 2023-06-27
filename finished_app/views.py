from django.shortcuts import render

# Create your views here.

app_name="finished_app"

def finished_app(request):
    return render(request,'finished_app/finished_app.html')