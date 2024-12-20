# from django.db import models
import jwt

from datetime import datetime, timedelta

from PostsService import settings 
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager, PermissionsMixin
)

from django.db import models








class UserManager(BaseUserManager):
    def create_user(self, username, password = None):
        if username is None:
            raise TypeError('Users must have a username.')
        
        user = self.model(
            username = username
        )

        user.set_password(password)
        user.save()
        return user 
    
    def create_superuser(self, username, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(
            username= username,
            password= password
        )

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user




class User(AbstractBaseUser, PermissionsMixin):    

    Gender = (
        ('male', 'male'),
        ('female', 'female')

    )

    username = models.TextField(
        verbose_name='имя',
        blank=True,
        unique=True
    )

    is_active = models.BooleanField(
        default=True
    )
    
    is_staff = models.BooleanField(
        default=False
    )

    bio = models.TextField(
        blank= True,
        null = True
    )

    github = models.CharField(
        max_length= 500,
        blank= True,
        null= True,
    )

    birthday = models.DateField(
        blank= True,
        null = True
    )

    gender = models.CharField(max_length= 6, choices=Gender)


    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    
    def get_full_name(self):
        return self.username
    

    class Meta:
        db_table = 'users'
