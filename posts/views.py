from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.views import APIView 

from .models import Posts
from .serializers import PostSerializer

# from photo.serializers import PhotoSerializers
# from document.serializers import DocumentSerializers
# from video.serializers import VideoSerializers

from .serializers import *






class SubViewPkMixin:

    def iteration_pk_posts(self, serial_data):
        for post in serial_data:
            posts_photos = PhotoSerializers2(
                Posts.objects.get(id = post['id']).photos.all(),
                many = True
            )
            posts_document = DocumentSerializers2(
                Posts.objects.get(id = post['id']).documents.all(),
                many = True
            )
            posts_video = VideoSerializers2(
                Posts.objects.get(id = post['id']).videos.all(),
                many = True 
            )
            post['photos'] = posts_photos.data
            post['documents'] = posts_document.data
            post['videos'] = posts_video.data
        return serial_data
    

    def get_list_request_file(self, request):
        req_data = dict(request.data.lists())
        file_dict = {}
        file_dict['photos'] = req_data.get('photos', None)
        file_dict['documents'] = req_data.get('documents', None)
        file_dict['videos'] = req_data.get('videos', None)

        return file_dict

    
    def serializer_sub_begin(self, request, post = None):
        if post is None:
            serializer = PostSerializer(data=request.data)
        else:
            serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            additional_data = self.get_list_request_file(request)
            if request.method != 'POST':
                additional_data['method'] = request.method
            serializer.save(**additional_data)
            return serializer
        else:
            return False




class PostListCreateAPIView(APIView, SubViewPkMixin):
       
    def get(self, request):
        posts = Posts.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(self.iteration_pk_posts(serializer.data))
    
    def post(self, request):
        if serializer := self.serializer_sub_begin(request):
            return Response(self.iteration_pk_posts([serializer.data]), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class PostDetailAPIView(APIView, SubViewPkMixin):
    def get_object(self, pk):
        try:
            return Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            return None

    def get(self, request, pk):
        if (post:=self.get_object(pk)) is None:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post)
        return Response(self.iteration_pk_posts([serializer.data]))


    def put(self, request, pk):
        if (post:=self.get_object(pk)) is None:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        if serializer := self.serializer_sub_begin(request, post):
            return Response(self.iteration_pk_posts([serializer.data]))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def patch(self, request, pk):
        if (post:=self.get_object(pk)) is None:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        if serializer := self.serializer_sub_begin(request, post):
            return Response(self.iteration_pk_posts([serializer.data]))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk):
        if (post:=self.get_object(pk)) is None:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



