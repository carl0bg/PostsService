from django.db import models





class Posts(models.Model):

    PRIVATE = 'private'
    PUBLIC = 'public'

    CHAT_TYPE = (
        (PRIVATE, 'private'),
        (PUBLIC, 'public'),
    )

    created_date = models.DateTimeField(
        auto_now_add = True,
        verbose_name = 'Время создание поста',
    )

    modified_date = models.DateTimeField(
        auto_now=True,
        verbose_name = 'Время изменения поста',
    )

    chat = models.CharField(
        max_length=55,
        default=PRIVATE,
        choices=CHAT_TYPE,
        verbose_name='Тип чата',
    )

    def __str__(self):
        return f'{self.id} - эл Posts'
    