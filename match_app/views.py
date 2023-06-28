from django.shortcuts import render

# Create your views here.



def match_app(request):
    return render(request,'match_app/match_app.html')