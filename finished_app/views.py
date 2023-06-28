from django.shortcuts import render

# Create your views here.



def finished_app(request):
    return render(request,'finished_app/finished_app.html')