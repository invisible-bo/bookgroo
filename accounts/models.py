import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False) 
    is_active = models.BooleanField(default=False)  
    activation_token = models.CharField(max_length=255, blank=True, null=True) 
    preferred_genres = models.ManyToManyField(Genre, blank=True, related_name="users")

    def __str__(self):
        return self.username
