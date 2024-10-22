from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import *
# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Image_Upload(request):
    
    files = request.FILES
    descriptions = request.data
    user = request.user
    try:
            
        if not files:
            return Response({'error': 'No files were uploaded'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not descriptions:
            return Response({'error': 'No descriptions provided'}, status=status.HTTP_400_BAD_REQUEST)
        alldata=[]
        for key, file in files.items():
            description_key = key.replace('[file]', '[description]')
            description = descriptions.get(description_key)

            if file and description and user.id:
                print(f"file:{file}",)
                print(f"Description: {description}")
                print('userid',user.id)
                data={
                        'user': user.id,
                        'image':file,
                        'descriptions':description
                    }
                if data:
                    alldata.append(data)
                        
                else:
                    return Response({'error': f'Missing file or description for {key}'}, status=400)
        print(alldata,'alldata')
        serializer = ImageSerializer(data=alldata,many=True)
        if serializer.is_valid():
            serializer.save()
                
            return Response("Successfully uploaded images",status=status.HTTP_200_OK)
            
        return Response({'error':serializer.errors})
    except Exception as e:
        return Response({'error':str(e)})
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Get_Image(request):
    
    user = request.user
    try:
        
      images = Images.objects.filter(user=user.id)
      serializer = ImageSerializer(images,many=True)
      return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)})