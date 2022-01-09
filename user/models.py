from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager


# Create your models here.

class MyUserManager(BaseUserManager):

    def create_user(self, username, email, password=None):

        if not username:
            raise TypeError('Users must have a username.')

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username = username,
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        email = email.lower()
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class MyUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=255, blank=False, null=False, unique=True)
    email = models.EmailField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "username"

    objects = MyUserManager()

    class Meta:
        db_table = "tbl_users"

    def __str__(self):
        return str(self.username)
        