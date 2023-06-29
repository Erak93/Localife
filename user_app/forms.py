from django import forms
from django.contrib.auth.models import User
from user_app.models import UserProfile, TravelerProfile, ExperienceTag, Experience, Booking, Review


class UserProfileForm(forms.ModelForm):           
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    
    class Meta:
        model = UserProfile
        fields = ('username','password', 'first_name', 'last_name', 'email', 'location', 'user_profile_image')
        labels = {
            
            'email': 'Email',
            'location': 'Location',
            'user_profile_image': 'Profile Image',
        }

  

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