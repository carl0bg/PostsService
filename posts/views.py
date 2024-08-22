from rest_framework import views, generics

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Posts
from .serializers import PostSerializers, PhotoSerializers


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers


class PostListView(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers



class PhotoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PhotoSerializers



class PhotoListView(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PhotoSerializers

    parser_classes = [MultiPartParser, FormParser]
    # @swagger_auto_schema(
    #     operation_description="Upload a photo for a post",
    #     manual_parameters=[
    #         openapi.Parameter(
    #             'post_id',
    #             openapi.IN_QUERY,
    #             description="ID of the post to which the photo belongs",
    #             type=openapi.TYPE_STRING,
    #             required=True,
    #         ),
    #         openapi.Parameter(
    #             'photo',
    #             openapi.IN_FORM,
    #             description="Photo file",
    #             type=openapi.TYPE_FILE,
    #             required=True,
    #         )
    #     ],
    #     responses={201: PhotoSerializers(many=False)}
    # )
    # def post(self, request, *args, **kwargs):
    #     super().post(self, request, *args, **kwargs)