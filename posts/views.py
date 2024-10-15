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


    def iteration_pk_posts(self, serial_data):
        for post in serial_data:
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
        return serial_data

        

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.serializer_class(queryset, many= True)
        
        return Response(self.iteration_pk_posts(serializer.data))

    def retrieve(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(self.iteration_pk_posts([serializer.data]))


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # if getattr(instance, '_prefetched_objects_cache', None):
        #     # If 'prefetch_related' has been applied to a queryset, we need to
        #     # forcibly invalidate the prefetch cache on the instance.
        #     instance._prefetched_objects_cache = {}

        return Response(self.iteration_pk_posts([serializer.data]))


    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
