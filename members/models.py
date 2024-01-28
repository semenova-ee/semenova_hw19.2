from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=50, unique=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True)
    phone_number = models.CharField(max_length=11, blank=True)
    country = models.CharField(max_length=50, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


