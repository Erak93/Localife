from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from user_app.forms import UserProfileForm, RegistrationForm,UserProfileLoginForm
from user_app.models import UserProfile
from django.contrib.auth.models import User
from django.db import transaction

def index(request):
    return HttpResponse('index')

def profile(request):
    #Get the loggen-in user

    user=request.user

    context={
        'user':user,
        
    }
    return render(request,'user_app/user_profile.html',context)

def registration_success(request):
    return HttpResponse('Registration successful!')

def register(request):
    """This function handles the registration"""
    registered = False

    if request.method == 'POST':
        user_form = RegistrationForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            with transaction.atomic():
                user = user_form.save(commit=False)
                user.set_password(user_form.cleaned_data['password'])
                user.save()

                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()

                UserProfile.objects.create(user=user)

            messages.success(request, 'Registration successful!')
            registered = True
            return redirect('user_app:success')
        else:
            error_message = 'Registration failed. Please check the form errors.'
            return render(request, 'user_app/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'error_message': error_message})

    else:
        user_form = RegistrationForm()
        profile_form = UserProfileForm()

    return render(request, 'user_app/registration.html', {
        'user_form': user_form,
        'profile_form': profile_form,
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


