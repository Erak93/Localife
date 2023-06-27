from django.shortcuts import render

# Create your views here.

app_name="user_app"

def user_app(request):
    return render(request,'user_app/user_app.html')

