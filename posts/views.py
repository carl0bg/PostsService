from rest_framework import views, generics

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Posts, Photo
from .serializers import PostSerializers, PhotoSerializers



class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers


class PostListView(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers



class PhotoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializers



class PhotoListView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializers

    parser_classes = [MultiPartParser, FormParser]
