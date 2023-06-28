from django.shortcuts import render

# I am adding the following from django level 5
from app_user.forms import NewUserForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.



def user_app(request):
    return render(request,'user_app/user_app.html')

# USER AUTHORIZATION HAPPENS IN VIEWS.PY

