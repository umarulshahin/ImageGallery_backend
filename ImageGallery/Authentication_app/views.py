from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


@api_view(['POST'])
def SignUp(request):
    print(request.data, 'resquest.data')
    data = request.data
    user= {
        'username' : data.get('username'),
        'email' : data.get('email'),
        'password' : data.get('password')
    }
    print(user,'user data')
    if user:
        serializer = RegisterSerializer(data=user)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': serializer.data},status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        
    return Response('User data required')

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token["role"]=user.is_superuser
        
        return token

class MyTokenobtainedPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer
    
