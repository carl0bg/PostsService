from django.db.models import Q

from .models import Follower


class FriendshipChecker:
    """
    Класс для проверки дружбы между пользователями.
    """
    @staticmethod
    def are_friends(user1, user2):
        friendship_count = Follower.objects.filter(
            Q(user=user1, subscriber=user2) | Q(user=user2, subscriber=user1)
        ).count()

        return friendship_count == 2