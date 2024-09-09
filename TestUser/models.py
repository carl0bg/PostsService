from django.db import models



class TestUser(models.Model):    
    tablename = ''

    username = models.TextField(
        verbose_name='имя',
        blank=True
    )
