from django.db import models
from accounts.models import CustomUser
from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    content = models.TextField(verbose_name='本文', blank=False, null=False)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural ='Post'

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("users:users_index")
        # return reverse("users:users_index", kwargs={'pk': self.pk})
