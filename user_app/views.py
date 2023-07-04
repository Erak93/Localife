from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from user_app.forms import UserProfileForm, RegistrationForm
from user_app.models import UserProfile
from django.contrib.auth.models import User

def index(request):
    return HttpResponse('index')

def registration_success(request):
    return HttpResponse('Registration successful!')

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


