from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    user_profile_image=serializers.ImageField(required=False)
    user_bio=serializers.CharField(required=False)
    class Meta:
        model = UserProfile
        fields = ['location', 'user_profile_image', 'user_bio']