from rest_framework import serializers
from .models import *
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['user', 'image', 'descriptions', 'created_at']
        read_only_fields = ['created_at']