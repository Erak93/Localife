from django.shortcuts import render

# Create your views here.

app_name="search_app"

def search_app(request):
    return render(request,'search_app/search_app.html')