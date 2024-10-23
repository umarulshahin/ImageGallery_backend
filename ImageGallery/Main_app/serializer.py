from rest_framework import serializers
from .models import *
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['id','user', 'image', 'descriptions', 'created_at','order']
        read_only_fields = ['created_at','id']
        
class ImageOrderSerializer(serializers.Serializer):
    
    id = serializers.IntegerField()
    order = serializers.IntegerField()

    
