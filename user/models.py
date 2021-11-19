from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

# Create your models here.


class MyUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=255, blank=False, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = "username"


    def __str__(self):
        return self.username
    
