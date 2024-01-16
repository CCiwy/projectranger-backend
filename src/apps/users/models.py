import hashlib

from django.contrib.auth.models import AbstractUser
from django.db import models

def hash_password(password):
    """ hash the password """
    return hashlib.sha256(password.encode()).hexdigest()


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=32, null=False)
    password = models.CharField(max_length=32, null=False)
    is_active = models.BooleanField(default=True)


    def set_password(self, raw_password):
        self.password = hash_password(raw_password)


    def check_password(self, raw_password):
        return self.password == hash_password(raw_password)



    def send_password_recovery_link(self):
        """ send password recovery link to user """
        # TODO: implement this method
        pass



class UserFriendShip(models.Model):
    """ model for user friendships """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')
    friend = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='friend')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Profile(models.Model):
    """ model for user profiles """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255)
    is_public = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





