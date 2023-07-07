from rest_framework import serializers
from user_app.models import Experience, Region, ExperienceTag, User


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('region_name', 'region_desc')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceTag
        fields = ('tag_name')

class HostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='UserProfile.username')
    class Meta:
        model = User
        fields = ('username')

class APISerializer(serializers.ModelSerializer):
    host = serializers.CharField(source='host.username')
    experience_tags = serializers.StringRelatedField(many=True)
    region = serializers.CharField(source='region.region_name')
    class Meta:
        model = Experience
        fields = "__all__" #('region_name', 'region_desc', 'region', 'experience_tags', 'host', 'title', 'description', 'start_date', 'end_date', 'price')

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('__all__')

