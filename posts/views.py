from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import action

from .models import Posts
from .serializers import PostSerializer

from photo.serializers import PhotoSerializers
from document.serializers import DocumentSerializers
from video.serializers import VideoSerializers


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

class PostListView(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer



class PostViewSet2(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.serializer_class(queryset, many= True)
        for post in serializer.data:
            posts_photos = PhotoSerializers(
                Posts.objects.get(id = post['id']).photos.all(),
                many = True
            )
            posts_document = DocumentSerializers(
                Posts.objects.get(id = post['id']).documents.all(),
                many = True
            )
            posts_video = VideoSerializers(
                Posts.objects.get(id = post['id']).videos.all(),
                many = True 
            )
            post['photos'] = posts_photos.data
            post['documents'] = posts_document.data
            post['videos'] = posts_video.data
        
        return Response(serializer.data)
        