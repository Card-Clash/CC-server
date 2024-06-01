from django.contrib.auth.models import AbstractUser
from django.db import models


class Player(AbstractUser):
    coins = models.IntegerField(default=0)
    permanent_ban = models.BooleanField(default=False)
