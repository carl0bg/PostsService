from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import PhotoSerializers
from .models import Photo


class PhotoDetailView(generics.RetrieveDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializers

class PhotoListView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializers

    parser_classes = [MultiPartParser, FormParser]