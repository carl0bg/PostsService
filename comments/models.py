from django.db import models
from django.conf import settings
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey

from posts.models import Posts

class AbstractComment(models.Model):
    '''Абстрактная модель для комментариев'''
    text = models.TextField(max_length=500)
    created_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.text}'

    class Meta:
        abstract = True



class Comment(AbstractComment, MPTTModel):
    '''модель комментариев'''
    user = models.ForeignKey(to = settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(to = Posts, related_name= 'comments', on_delete=models.CASCADE)
    parent = TreeForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null= True,
        blank= True,
        related_name='children'
    )

    def __str__(self):
        return f'{self.user} - {self.post}'
    
