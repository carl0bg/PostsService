from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from rest_framework.decorators import action, parser_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.views import APIView 
from rest_framework import generics, mixins

from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema


from .models import Posts
from .serializers import PostSerializer

from .serializers import *






# class SubViewPkMixin:

#     def iteration_pk_posts(self, serial_data):
#         for post in serial_data:
#             posts_photos = PhotoSerializers(
#                 Posts.objects.get(id = post['id']).photos.all(),
#                 many = True
#             )
#             posts_document = DocumentSerializers(
#                 Posts.objects.get(id = post['id']).documents.all(),
#                 many = True
#             )
#             posts_video = VideoSerializers(
#                 Posts.objects.get(id = post['id']).videos.all(),
#                 many = True 
#             )
#             post['photos'] = posts_photos.data
#             post['documents'] = posts_document.data
#             post['videos'] = posts_video.data
#         return serial_data
    

#     def get_list_request_file(self, request):
#         req_data = dict(request.data.lists())
#         file_dict = {}
#         file_dict['photos'] = req_data.get('photos', None)
#         file_dict['documents'] = req_data.get('documents', None)
#         file_dict['videos'] = req_data.get('videos', None)

#         return file_dict

    
#     def serializer_sub_begin(self, request, post = None):
#         if post is None:
#             serializer = PostSerializer(data=request.data, context={'request': request})
#         else:
#             serializer = PostSerializer(post, data=request.data)
#         # serializer.user = request.user
#         if serializer.is_valid():
#             additional_data = self.get_list_request_file(request)
#             # additional_data['user'] = request.user
#             if request.method != 'POST':
#                 additional_data['method'] = request.method
#             serializer.save(**additional_data)
#             return serializer, True
#         else:
#             return serializer, False




# class PostListCreateAPIView(APIView, SubViewPkMixin):

#     # permission_classes = [IsAuthenticatedOrReadOnly]


#     def get(self, request):
#         posts = Posts.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(self.iteration_pk_posts(serializer.data))
    

#     @swagger_auto_schema(
#         operation_description="Создание поста",
#         request_body=PostSerializer,
#         responses={201: PostSerializer(many=False)}
#     )
#     def post(self, request):
#         serializer, flag_valid = self.serializer_sub_begin(request)
#         if flag_valid:
#             return Response(self.iteration_pk_posts([serializer.data]), status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class PostDetailAPIView(APIView, SubViewPkMixin):

#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def get_object(self, pk):
#         try:
#             return Posts.objects.get(pk=pk)
#         except Posts.DoesNotExist:
#             return None

#     def get(self, request, pk):
#         if (post:=self.get_object(pk)) is None:
#             return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = PostSerializer(post)
#         return Response(self.iteration_pk_posts([serializer.data]))



#     @swagger_auto_schema(
#         operation_description="Put Post",
#         request_body=PostSerializer,
#     )
#     def put(self, request, pk):
#         if (post:=self.get_object(pk)) is None:
#             return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

#         serializer, flag_valid = self.serializer_sub_begin(request, post)
#         if flag_valid:
#             return Response(self.iteration_pk_posts([serializer.data]))
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     @swagger_auto_schema(
#         operation_description="Patch Post",
#         request_body=PostSerializer,
#     )
#     def patch(self, request, pk):
#         if (post:=self.get_object(pk)) is None:
#             return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

#         serializer, flag_valid = self.serializer_sub_begin(request, post)
#         if flag_valid:
#             return Response(self.iteration_pk_posts([serializer.data]))
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#     def delete(self, request, pk):
#         if (post:=self.get_object(pk)) is None:
#             return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



class PostListCreateAPIView(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    # def get_queryset(self):


    # def create(self, request):
    #     serializer, flag_valid = self.serializer_sub_begin(request)
    #     if flag_valid:
    #         return Response(self.iteration_pk_posts([serializer.data]), status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def retrieve(self, request, pk=None):
    #     page = get_object_or_404(Posts, pk=pk)
    #     queryset = Posts.objects.get(id = pk)
    #     serializer = PostSerializer(queryset, many=False)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    


    #     def post(self, request):
#         serializer, flag_valid = self.serializer_sub_begin(request)
#         if flag_valid:
#             return Response(self.iteration_pk_posts([serializer.data]), status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)