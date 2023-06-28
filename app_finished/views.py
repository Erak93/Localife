from django.shortcuts import render

# Create your views here.



def app_finished(request):
    return render(request,'app_finished/app_finished.html')