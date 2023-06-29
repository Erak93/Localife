from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from user_app.forms import UserProfileForm
from user_app.models import UserProfile

def index(request):
    return HttpResponse('index')

def registration_success(request):
    return HttpResponse('Registration successful!')

def register(request):
    """This function is handling the registration"""
    registered = False

    if request.method == 'POST':
        user_form = UserProfileForm(data=request.POST)

        if user_form.is_valid():
            username= user_form.cleaned_data['username']
            

            if UserProfile.objects.filter(username=username).exists():
                error_message = 'Username already exists. Please choose a different username.'
                return render(request, 'user_app/registration.html', {'user_form': user_form, 'error_message': error_message})

            # Create the UserProfile instance and assign the user_id field
            user = user_form.save()
            profile = UserProfile()
            profile.user = user
            profile.save()

            messages.success(request, 'Registration successful!')

            registered = True
            return redirect('registration_success')

    else:
        user_form = UserProfileForm()

    return render(request, 'user_app/registration.html', {
        'user_form': user_form,
        'registered': registered
    })

def user_login(request):
    """This function is required for the login"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('login')  # Replace 'login' with the correct URL name
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')

        else:
            print('Someone tried to login and failed!')
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")

    else:
        return render(request, 'user_app/login.html', {})


