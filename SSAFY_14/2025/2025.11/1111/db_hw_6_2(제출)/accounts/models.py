from django.db import models
from django.contrib.auth.models import AbstractUser


# User:User의 M:N 관계가 형성되도록 작성
# 단, M이 N과 관계를 맺어도 N은 M과 관계가 맺어지지 않아야 한다. (비대칭 관계)
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')