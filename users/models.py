from django.db import models


# Create your models here.
class UsersRelation(models.Model):
    
    # import CustomUserで参照しようとするとエラーが出るため、第一引数はpathを使用すること
    follower = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE, related_name='followers_relation')

    following = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE, related_name='followings_relation')

    class Meta:
        unique_together = ('follower', 'following')
