from rest_framework import generics, permissions, views
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend, FilterSet # Включите FilterSet

from .models import Follower
from .serializers import ListFollowerOnSerializer, ListFollowerSerializer
from TestUser.models import User


class ListFollowerView(generics.ListAPIView):
    """ Вывод списка своих подписчиков
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListFollowerSerializer

    def get_queryset(self):
        return Follower.objects.filter(user=self.request.user)



class AddFollowerView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]


    def post(self, request, pk):
        '''Подписаться на пользователя(pk)'''
        try:
            user = User.objects.get(id = pk)
            if user.id is request.user.id:
                return Response(status=401, data = {'error': 'Запрещено подписаться на самого себя'})
            elif Follower.objects.filter(user = user.id, subscriber = request.user.id).exists():
                return Response(status= 401, data= {'error': 'Пользователь уже подписан'})
        except User.DoesNotExist: 
            return Response(status=404, data = {'error': 'Данный пользователь не найден'})
        Follower.objects.create(subscriber = request.user, user = user)
        return Response(status=201)
    

class DeleteFollowerView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        '''Удалиться из подписчиков'''
        try:
            subj = Follower.objects.get(user_id = pk, subscriber_id = request.user.id)
        except Follower.DoesNotExist:
            return Response(status=404, data = {'error': 'Ошибка в подписке'})
        subj.delete()
        return Response(status=204)
    

class IsFollowerToView(generics.ListAPIView):
    """ Вывод списка на кого подписан пользователь
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListFollowerOnSerializer

    def get_queryset(self):
        return Follower.objects.filter(subscriber=self.request.user)
