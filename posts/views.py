from rest_framework import generics, viewsets
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from .models import Posts
from .serializers import PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

class PostListView(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer



class PostViewSet2(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    # parser_classes = [MultiPartParser, FormParser]

