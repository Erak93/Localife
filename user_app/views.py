from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from user_app.forms import UserProfileForm

def index(request):
    return HttpResponse('index')

def register(request):
    """ This function is handling the registration"""
    registered = False

    if request.method == 'POST':                              
        user_form = UserProfileForm(data=request.POST)          # creating a variable of the object

        if user_form.is_valid():                                # if the object is already created
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password']) 
            user.save()                                         #save to the internally database

            registered = True                                       
            return redirect('registration_success')  # Redirect to a success page 
            

    else:
        user_form = UserProfileForm()                               # create a object (because not registered yet)

    return render(request, 'user_app/registration_success.html', {         # storing the data
        'user_form': user_form,
        'registered': registered
    })                                                              

def user_login(request):
    """ This function is required for the login"""                                                                
    if request.method == 'POST':                                    # if the user is sending data
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password) # checks if the user exist

        if user is not None:                                                # if user exist
            if user.is_active:
                login(request, user)                                                # login
                return redirect('login')  # Redirect to the desired page after login///// HUGE_BUG
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')                           #fuck the user

        else:                                                                       #if user is none
            print('Someone tried to login and failed!')
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")                  #fuck him

    else:
        return render(request, 'user_app/login.html', {})                           #login site                  
        

