from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    followings = models.ManyToManyField("CustomUser", verbose="フォロー中のユーザー", through="UsersRelation", related_name="+", through_fields=('following', 'follower'))

    followers = models.ManyToManyField("CustomUser", verbose="フォローされているユーザー", through="UsersRelation", related_name="+", through_fields=('follower', 'following'))
    
    class Meta:
        verbose_name_plural = 'CustomUser'
