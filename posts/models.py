from django.db import models
from accounts.models import CustomUser


class Post(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT, related_name='post')
    content = models.TextField(verbose_name='本文', blank=False, null=False)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural ='Post'

    def __str__(self):
        return self.content
