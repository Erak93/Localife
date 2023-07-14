from rest_framework import serializers
from user_app.models import Experience

class ExperienceSerializer(serializers.ModelSerializer):
    experience_image = serializers.ImageField(required=False)

    class Meta:
        model = Experience
        fields = '__all__'


    #no need to use this one>>>
    
    # def validate(self, data):
    #     if data['password'] != data['password2']:
    #         return serializers.ValidationError("Passwords must match.")
    #     return data
    
    # def create(self, validated_data):
    #     experience = Experience.objects.create(**validated_data)
    #     experience.other = validated_data.get('other', experience.other)
    #     experience.save()
    #     return experience

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.other = validated_data.get('other', instance.other)
    #     instance.save()
    #     return instance