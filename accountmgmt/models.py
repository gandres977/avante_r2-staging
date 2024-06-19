from django.contrib.auth.models import AbstractUser
from django.db import models


class AvanteUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=100)
