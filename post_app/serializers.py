from rest_framework import serializers
from user_app.models import Experience

class ExperienceSerializer(serializers.ModelSerializer):
    experience_image = serializers.ImageField(required=False)
    class Meta:
        model = Experience
        fields = '__all__'

# class ExperienceImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Experience
#         fields = ['id', 'experience_image']


    #no need to use this one>>>
    
    # def validate(self, data):
    #     if data['password'] != data['password2']:
    #         return serializers.ValidationError("Passwords must match.")
    #     return data
    
 