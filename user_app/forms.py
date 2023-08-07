from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from user_app.models import UserProfile, TravelerProfile, ExperienceTag, Experience, Booking, Review


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'pattern': '[\w.@+-]+', 'title': 'Username should only contain letters, digits, and @/./+/-/_ characters.'})
    )
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model= User
        fields = ('username', 'first_name', 'last_name', 'email')



class UserProfileForm(forms.ModelForm):           
    
    class Meta:
        model = UserProfile
        fields = ('location', 'user_profile_image')
        labels = {
            
    
            'location': 'Location',
            'user_profile_image': 'Profile Image',
        }

class UserProfileLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    
  

class TravelerProfileForm(forms.ModelForm):
    class Meta:
        model = TravelerProfile
        fields = []

class ExperienceTagForm(forms.ModelForm):
    class Meta:
        model = ExperienceTag
        fields = ['tag_name']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'description', 'price', 'experience_tags', 'experience_image']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['traveler', 'experience', 'start_date', 'end_date']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'listing', 'rating', 'comment']