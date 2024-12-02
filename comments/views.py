from rest_framework import permissions, generics

from .base.classes import CreateUpdateDestroy, CreateRetrieveUpdateDestroy
from .base.permissions import IsAuthor
from .models import Posts, Comment
from .serializers import (PostSerializer2, ListPostSerializer, CreateCommentSerializers)


class PostListView(generics.ListAPIView):
    """ Список public постов на стене пользователя
    """
    serializer_class = ListPostSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Posts.objects.filter(
            user_id=self.kwargs.get('pk'),
            chat = Posts.ChatType.PRIVATE
        ).select_related('user').prefetch_related('comments', 'photos', 'documents', 'videos')
    




class PostView(CreateRetrieveUpdateDestroy):
    """ CRUD поста
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Posts.objects.all().select_related('user').prefetch_related('comments')
    serializer_class = PostSerializer2
    permission_classes_by_action = {
        'get': [permissions.AllowAny],
        'update': [IsAuthor],
        'destroy': [IsAuthor]
        }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentsView(CreateUpdateDestroy):
    """ CRUD комментариев 
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializers
    permission_classes_by_action = {
        'update': [IsAuthor],
        'destroy': [IsAuthor]
        }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()