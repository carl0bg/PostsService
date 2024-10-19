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






class PostListCreateAPIView(APIView):
    def get(self, request, format=None):
        posts = Posts.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            # additional_data = {"photos": request.data['photos']}
            additional_data = {"photos": dict((request.data).lists())['photos']}
            serializer.save(**additional_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PostDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        if post is None:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        if post is None:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        if post is None:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







# class PostsListView3(APIView):
#     """Вывод списка фильмов"""
#     def get(self, request):
#         movies = Posts.objects.all()
#         serializer = PostSerializer3(movies, many=True)
#         return Response(serializer.data)


# class PostsDetailView3(APIView):
#     """Вывод фильма"""
#     def get(self, request, pk):
#         movie = Posts.objects.get(id=pk)
#         serializer = PostSerializer3(movie)
#         return Response(serializer.data)


# class ReviewCreateView3(APIView):
#     """Добавление отзыва к фильму"""
#     def post(self, request):
#         review = PostSerializer3(data=request.data)
#         if review.is_valid():
#             review.save()
#         return Response(status=201)
    


# class PostViewSet3_sets(viewsets.ModelViewSet):
#     queryset = Posts.objects.all()
#     serializer_class = PostSerializer3







# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Posts.objects.all()
#     serializer_class = PostSerializer

# class PostListView(generics.ListCreateAPIView):
#     queryset = Posts.objects.all()
#     serializer_class = PostSerializer





# class PostViewSet2(viewsets.ModelViewSet):
#     queryset = Posts.objects.all()
#     serializer_class = PostSerializer


#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def iteration_pk_posts(self, serial_data):
    #     for post in serial_data:
    #         posts_photos = PhotoSerializers2(
    #             Posts.objects.get(id = post['id']).photos.all(),
    #             many = True
    #         )
    #         posts_document = DocumentSerializers2(
    #             Posts.objects.get(id = post['id']).documents.all(),
    #             many = True
    #         )
    #         posts_video = VideoSerializers2(
    #             Posts.objects.get(id = post['id']).videos.all(),
    #             many = True 
    #         )
    #         post['photos'] = posts_photos.data
    #         post['documents'] = posts_document.data
    #         post['videos'] = posts_video.data
    #     return serial_data

        

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.serializer_class(queryset, many= True)
        
    #     return Response(self.iteration_pk_posts(serializer.data))

    # def retrieve(self, request, pk=None):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(self.iteration_pk_posts([serializer.data]))


    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
  
    #     return Response(self.iteration_pk_posts([serializer.data]))


    # def partial_update(self, request, *args, **kwargs):
    #     kwargs['partial'] = True
    #     return self.update(request, *args, **kwargs)
    
