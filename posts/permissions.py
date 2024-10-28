from rest_framework import permissions
from .models import Posts


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Позволяет удалять объект только его создателю
    """

    def has_object_permission(self, request, view, obj: Posts):
        if request.method in permissions.SAFE_METHODS: #(GET, HEAD, OPTIONS) для всех пользователей
            return True
        
        return obj.user == request.user



class IsOnlyOwner(permissions.BasePermission):
    """
    Действия только для владельцев обьекта
    """

    def has_object_permission(self, request, view, obj: Posts):        
        return obj.user == request.user