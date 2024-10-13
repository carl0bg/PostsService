from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import action

from .models import Posts
from .serializers import PostSerializer
from photo.serializers import PhotoSerializers


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
        # serializer = self.get_serializer(queryset, many=True)
        serializer = self.serializer_class(queryset, many= True)
        for post in serializer.data:
            # print(post.photo, post.photo['file'])
            perem = Posts.objects.get(id = post['id']).photos.all()
            perem2 = PhotoSerializers(perem, many = True)
            post['photos'] = perem2.data
        return Response(serializer.data)
        