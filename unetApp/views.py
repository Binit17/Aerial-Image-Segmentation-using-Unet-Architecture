from django.shortcuts import render
from .serializers import ImageSerializer
from .models import Images
from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework.response import Response

# Create your views here.

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer
    
    # def post(self, request, *args, **kwargs):
    #     unMaskedImage = request.data['unMaskedImage']
    #     Images.objects.create(unMaskedImage =unMaskedImage)
    #     return HttpResponse({'message':'Image Uploaded.'}, status = 200)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'message': 'Image uploaded successfully', 'unMaskedImage': serializer.data['unMaskedImage']}, status=status.HTTP_201_CREATED, headers=headers)