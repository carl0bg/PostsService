from rest_framework import serializers

from .recursiv_serializers import *
from .models import Comment

from posts.models import Posts
from photo.serializers import PhotoSerializers
from video.serializers import VideoSerializers
from document.serializers import DocumentSerializers


class CreateCommentSerializers(serializers.ModelSerializer):
    '''Добавление коментариев к посту'''
    class Meta:
        model = Comment
        fields = ('post', 'text', 'parent') 


class ListCommentSerializer(serializers.ModelSerializer):
    '''Список коментариев'''
    text = serializers.SerializerMethodField()
    children = RecursiveSerializer(many = True)

    def get_text(self, obj: Comment):
        if obj.deleted:
            return None
        return obj.text
    
    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ("id", "post", "user", "text", "created_data", "update_data", "deleted", "children")


    

class PostSerializer2(serializers.ModelSerializer):
    '''Вывод поста'''  
    user = serializers.ReadOnlyField(source = 'user.username')
    comments = ListCommentSerializer(many = True, read_only = True)
    view_count = serializers.CharField(read_only = True)

    class Meta:
        model = Posts
        # fields = ("id", "created_date", "user", "text", "comments", "view_count")
        fields = "__all__"



class ListPostSerializer(serializers.ModelSerializer):
    '''Список постов'''
    user = serializers.ReadOnlyField(source= 'user.username')
    photos = PhotoSerializers(many=True, read_only=True)
    documents = DocumentSerializers(many = True, read_only = True)
    videos = VideoSerializers(many = True, read_only = True)

    class Meta:
        model = Posts
        fields = ("id", "created_date", "user", "text", "photos", 'documents', 'videos', "comments_count")