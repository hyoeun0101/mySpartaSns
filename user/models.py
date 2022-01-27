from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class UserModel(AbstractUser):  # 추가적인 코드없이 괄호에 있는 클래스 사용할 수 있다.
    class Meta:
        db_table = 'my_user'

    bio = models.CharField(max_length=256, default='')
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='followee')
    #내가 팔로우함. 반대로 상대방은 팔로워가 추가된것
