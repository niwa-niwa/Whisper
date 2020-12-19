from accounts.models import CustomUser
from django.db import models

# Create your models here.
class UsersRelation(models.Model):
    follower = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='following')

    following = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='follower')

    class Meta:
        unique_together = ('follower', 'following')
