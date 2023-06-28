# we need to create a serialize model to convert objects into items that can respond to API requests

from rest_framework import serializers
from user_app.models import Experience

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Experience
        fields='__all__'