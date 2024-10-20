from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def SignUp(request):
    print(request.data, 'resquest.data')
    return Response('yes working')


