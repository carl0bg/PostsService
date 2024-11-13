from rest_framework import generics, permissions, views
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend, FilterSet # Включите FilterSet

from .models import Follower
from .serializers import ListFollowerSerializer
from TestUser.models import User


# class ListFollowerView(generics.ListAPIView):
#     '''Вывод списка подписчиков пользователей'''

#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = ListFollowerSerializer
    
#     def get_queryset(self):
#         return Follower.objects.filter(user = self.request.user) #найдем всех его подписчиков



# class ListFollowerView(generics.ListAPIView):
#     """ Вывод списка подписчиков пользователя
#     """
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = ListFollowerSerializer

#     def get_queryset(self):
#         return Follower.objects.filter(user=self.request.user)

# class FollowerFilter(FilterSet):
#     class Meta:
#         model = Follower  # Ваша модель Follower
#         fields = ['user']  # Поле, по которому будет фильтроваться


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
            elif not Follower.objects.filter(id = user.id).exists():
                return Response(status= 401, data= {'error': 'Пользователь уже подписан'})
        except User.DoesNotExist:  #проверить
            return Response(status=404, data = {'error': 'Данный пользователь не найден'})
        Follower.objects.create(subscriber = request.user, user = user)
        return Response(status=201)
    

    def delete(self, request, pk):
        '''удаление из подписчиков'''
        try:
            subj = Follower.objects.get(id = pk)
        except Follower.DoesNotExist:
            return Response(status=404)
        subj.delete()
        return Response(status=204)