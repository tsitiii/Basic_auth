from django.shortcuts import render, redirect
from .models import Library  
from .serializers import ImageSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

def index(request):
    # photos = Library.objects.all()  # Fetch all photos
    if request.method == "POST":
        return redirect('photos/home.html')
    return render(request, 'photo/upload.html')  

def home(request):
    photos = Library.objects.all()
    return render(request, 'photo/home.html')

class ImageViewSet(ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
