from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=32, null=False)
    bio = models.CharField(max_length=255)
    is_public = models.BooleanField(default=False)



class Profile(models.Model):
    """ model for user profiles """
    user = 

