from django.db import models



class TestUser(models.Model):    

    username = models.TextField(
        verbose_name='имя',
        blank=True
    )

    class Meta:
        db_table = 'users'
