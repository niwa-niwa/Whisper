from django.db import models
from django.contrib.auth.models import AbstractUser
from users.models import UsersRelation


class CustomUser(AbstractUser):
    
    followings = models.ManyToManyField('CustomUser', verbose_name="フォロー中のユーザー", through=UsersRelation, related_name='+',  through_fields=('follower', 'following'))

    followers = models.ManyToManyField('CustomUser', verbose_name="フォローされているユーザー", through=UsersRelation, related_name='+', through_fields=('following', 'follower'))

    class Meta:
        verbose_name_plural = 'CustomUser'
