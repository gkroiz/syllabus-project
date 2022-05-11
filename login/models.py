from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _

# Constant for the types of users (actual value, human readable name)
USER_TYPE = (
    ('student', 'Student'),
    ('faculty', 'Faculty'),
    ('dept', 'Department')
)

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,

        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True, default="")
    user_type = models.CharField(max_length=10, choices=USER_TYPE, default='student')

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    objects = MyAccountManager()
    def __str__(self):
        return self.email
        # For checking permissions. to keep it simple all admin have ALL permissons

    def has_module_perms(self, app_label):
        return True

    # objects = CustomUserManager()
