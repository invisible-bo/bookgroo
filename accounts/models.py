import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_active = models.BooleanField(default=False)  
    activation_token = models.CharField(max_length=255, blank=True, null=True) 

    def __str__(self):
        return self.username
