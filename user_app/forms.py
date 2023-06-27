from django import forms
from user_app.models import UserProfile, TravelerProfile, ExperienceTag, Experience, Booking, Review




class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['location', 'user_profile_image']

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