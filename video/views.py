
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated

from .serializers import VideoSerializers
from .models import Video


class VideoDetailView(generics.RetrieveDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers

    permission_classes = [IsAuthenticated,]





class VideoListView(generics.CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers
    # permission_classes = IsAuthenticated

    parser_classes = [MultiPartParser, FormParser]