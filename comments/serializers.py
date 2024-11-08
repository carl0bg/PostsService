from rest_framework import serializers

from .recursiv_serializers import *
from .models import Comment

from posts.models import Posts


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
        fields = ("id", "post", "user", "text", "created_date", "update_date", "deleted", "children")
    

class PostSerializer(serializers.ModelSerializer):
    '''Вывод поста'''  
    user = serializers.ReadOnlyField(source = 'user.username')
    comments = ListCommentSerializer(many = True, read_only = True)
    view_count = serializers.CharField(read_only = True)

    class Meta:
        model = Posts
        fields = ("id", "created_date", "user", "text", "comments", "view_count")


class ListPostSerializer(serializers.ModelSerializer):
    '''Список постов'''
    user = serializers.ReadOnlyField(source= 'user.username')

    class Meta:
        model = Posts
        fields = ("id", "create_date", "user", "text", "comments_count")