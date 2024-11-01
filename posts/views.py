from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from rest_framework.decorators import action, parser_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework import generics, mixins

from drf_yasg.utils import swagger_auto_schema


from .models import Posts
from .serializers import PostSerializer
from .permissions import IsOnlyOwner, IsOwnerOrReadOnly






class SubViewPkMixin:

    def get_list_request_file(self, request):
        req_data = dict(request.data.lists())
        file_dict = {}
        file_dict['photos'] = req_data.get('photos', None)
        file_dict['documents'] = req_data.get('documents', None)
        file_dict['videos'] = req_data.get('videos', None)

        return file_dict

    
    def serializer_sub_begin(self, request, post = None):
        if post is None:
            serializer = PostSerializer(data=request.data, context={'request': request})
        else:
            serializer = PostSerializer(post, data=request.data)
        serializer.user = request.user
        if serializer.is_valid():
            additional_data = self.get_list_request_file(request)
            additional_data['user'] = request.user
            if request.method != 'POST':
                additional_data['method'] = request.method
            serializer.save(**additional_data)
            return serializer, True
        else:
            return serializer, False



class PostListAPIView(generics.ListAPIView):
    '''Получить весь список Post'''
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .select_related('user')  # Пример для ForeignKey к пользователю
            .prefetch_related('documents', 'photos', 'videos')
        )



class PostGetOneAPIView(generics.RetrieveUpdateAPIView, SubViewPkMixin):
    '''GET, PUT, PATCH отдельного элемента Post'''
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    @swagger_auto_schema(
        operation_description="Put Post",
        request_body=PostSerializer,
    )
    def put(self, request, pk):
        if (post:=self.get_object()) is None:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer, flag_valid = self.serializer_sub_begin(request, post)
        if flag_valid:
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    @swagger_auto_schema(
        operation_description="Patch Post",
        request_body=PostSerializer,
    )
    def patch(self, request, pk):
        if (post:=self.get_object()) is None:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer, flag_valid = self.serializer_sub_begin(request, post)
        if flag_valid:
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




class PostCreateAPIView(generics.CreateAPIView, SubViewPkMixin):
    '''Создать объект'''
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Создание поста",
        request_body=PostSerializer,
        responses={201: PostSerializer(many=False)}
    )
    def post(self, request):
        serializer, flag_valid = self.serializer_sub_begin(request)
        if flag_valid:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PostDeleteView(generics.DestroyAPIView):
    '''удаление post'''
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOnlyOwner]
