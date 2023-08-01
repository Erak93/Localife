from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from user_app.forms import UserProfileForm, RegistrationForm,UserProfileLoginForm
from user_app.models import UserProfile
from django.contrib.auth.models import User
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework import generics, status
from search_app.models import Booking
from user_app.models import Experience
from django.shortcuts import render,get_object_or_404
import time
from django.urls import reverse


class UserProfileUpdate(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    #permission_classes = [IsAuthenticated]

"""
class UserProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(user_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        """

def index(request):
    return HttpResponse('index')

def profile(request):
    #Get the loggen-in user

    user=request.user
    booking_listing = Booking.objects.all()
    experience_listing=Experience.objects.all()
    if user.id==None or user.id-1<=0:
        return HttpResponse("Create profile")
    else:
        context={
            'user':user,
            'user_id':user.id-1,
            'booking_listing':booking_listing,
            'experience_listing':experience_listing
            
            
        }
        print(user.id)
        return render(request,'user_app/user_profile.html',context)

def extract_id(name):
    experience = Experience.objects.get(title=name)
    return experience.id



def registration_success(request):
   
    # Redirect to the login page
    
    return render(request,'registration/login.html')

def register(request):
    """This function handles the registration"""
    registered = False

    if request.method == 'POST':
        user_form = RegistrationForm(data=request.POST)

        if user_form.is_valid():
            # Save the user_form before checking for username existence
            

            username = user_form.cleaned_data['username']

            if User.objects.filter(username=username).exists():

                error_message = 'Username already exists. Please choose a different username.'
                user.delete()  # Delete the user if username exists
                return render(request, 'user_app/registration.html', {'user_form': user_form, 'error_message': error_message})
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            # new_user.set_password(user_form.cleaned_data['password'])
            # Create the UserProfile instance and assign the user_id field
            
            UserProfile.objects.create(user=user)
            messages.success(request, 'Registration successful!')

            registered = True
            return redirect('user_app:success')

    else:
        user_form = RegistrationForm()

    return render(request, 'user_app/registration.html', {
        'user_form': user_form,
        'registered': registered
    })

def user_login(request):
    if request.method == 'POST':
        form = UserProfileLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    
                    return redirect('home_app')  # Replace 'home_app' with the correct URL name
                else:
                    return HttpResponse('ACCOUNT NOT ACTIVE')
            else:
                print('Someone tried to login and failed!')
                print("Username: {} and password {}".format(username, password))
                return HttpResponse("Invalid login details supplied!")
    else:
        form = UserProfileLoginForm()
    
    return render(request, 'user_app/login.html', {'form': form})

