from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
from django.contrib.auth import get_user_model
# Create your models here.

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title