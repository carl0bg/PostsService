from rest_framework import permissions, viewsets
from rest_framework.response import Response

from comments.base.classes import MixedPermission
from comments.serializers import PostSerializer2
from posts.serializers import ListPostSerializer
from .services import feed_service


class WallView(viewsets.GenericViewSet):
    serializer_class = ListPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = feed_service.get_post_list(request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, *args, **kwargs):
        instance = feed_service.get_single_post(kwargs.get('pk'))
        serializer = PostSerializer2(instance)
        return Response(serializer.data)