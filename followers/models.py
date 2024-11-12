from django.db import models
from django.conf import settings


class Follower(models.Model):
    '''Модель подписчиков'''
    user = models.ForeignKey(
        to = settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name = 'owner'
    )
    subscriber = models.ForeignKey(
        to = settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='subscribers'
    )


    class Meta:
        db_table = 'follower'
