
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import VideoSerializers

from .models import Video


class VideoDetailView(generics.RetrieveDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers




class VideoListView(generics.CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers

    parser_classes = [MultiPartParser, FormParser]