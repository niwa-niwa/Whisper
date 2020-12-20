from django.db import models
from django.contrib.auth.models import AbstractUser
from users.models import UsersRelation
from django.apps import apps
from itertools import chain



class CustomUser(AbstractUser):
    
    followings = models.ManyToManyField('CustomUser', verbose_name="フォロー中のユーザー", through=UsersRelation, related_name='+',  through_fields=('follower', 'following'))

    followers = models.ManyToManyField('CustomUser', verbose_name="フォローされているユーザー", through=UsersRelation, related_name='+', through_fields=('following', 'follower'))

    class Meta:
        verbose_name_plural = 'CustomUser'

    
    # ユーザーの投稿をすべて取得
    def getPosts(self):
        post_model = apps.get_model('posts', 'Post')
        posts = post_model.objects.filter(user=self).order_by('-created_at')
        return posts

    def timeLine(self):
        user = CustomUser.objects.filter(id=self.id)
        followings = self.followings.values_list("id", flat=True)
        result_list =list(chain(user, followings))
        post_model = apps.get_model('posts', 'Post')
        posts = post_model.objects.filter(user__in=result_list).order_by('-created_at')

        return posts


    # # ユーザーがフォローしているユーザー取得
    # def getFollowings(self):
    #     users_relation = apps.get_model('users', 'UsersRelation')
    #     followings = users_relation.objects.filter(follower=self).only('following')
    #     print(vars(followings))
    #     return followings


    # # ユーザーをフォローしているユーザー取得
    # def getFollowers(self):
    #     users_relation = apps.get_model('users', 'UsersRelation')
    #     followers = users_relation.objects.filter(following=self)
    #     return followers

