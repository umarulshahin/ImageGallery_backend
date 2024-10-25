from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
import random
from django.core.mail import send_mail
from django.core.cache import cache

@api_view(['POST'])
def SignUp(request):
    
    data = request.data
    user= {
        'username' : data.get('username'),
        'email' : data.get('email'),
        'password' : data.get('password')
    }
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
    
@api_view(['POST'])    
def Forget_password(request):
    
    email = request.data.get('email')
    if email:
        try:
            user = CustomUser.objects.filter(email = email).first()
            if user:
                otp = random.randint(100000, 999999)
                subject="Image Gallery OTP verification"
                message = f'Your OTP code is {otp}. It is valid for 3 minutes.'
                from_email = 'akkushahin666@gmail.com'
                recipient_list = ['akkushahin666@gmail.com']
                send_mail(subject, message, from_email, recipient_list,fail_silently=False)
                cache.set(f'otp_{email}',otp,timeout=180)
                
                return Response({"message": "OTP sent successfully", "email":email})
            else:
            
                return Response({'error': 'User with this email does not exist'}, status=status.HTTP_404_NOT_FOUND)
                
        except Exception as e:
            
            return Response({'error':e},status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response('User email is required')
    
@api_view(['POST'])
def OTP_validation(request):
    
    email = request.data.get('email')
    otp = request.data.get('otp')
    
    
    if not email or not otp:
        return Response ("OTP and Email is required",status=status.HTTP_404_NOT_FOUND)
    try:
        
        stored_otp = cache.get(f'otp_{email}')
        
        if not stored_otp:
            return Response({'error':'OTP expired or not found'},status=status.HTTP_404_NOT_FOUND)
        if str(stored_otp) == str(otp):
            return Response({'message':'OTP successfull','email':email},status=status.HTTP_200_OK)
        else:
            return Response({'error':'Invalid OTP'},status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
        
        return Response({'error':e},status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])    
def NewPassword(request):
    
    data = request.data

    try:
        formdata = {
            'email': data.get('email'),
            'password': data.get('password')
        }

        if not all(formdata.values()):
            return Response("Email and password are required", status=status.HTTP_400_BAD_REQUEST)
        data = CustomUser.objects.filter(email=formdata['email']).first()
        serializer = ForgetPasswordSerializer(data,formdata,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)

        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        print(f'error {e}')
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
