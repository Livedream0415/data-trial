from django.db import models
from django.utils import timezone
# Create your models here.


class User(models.Model):
    # username password_hash timestamp
    username = models.CharField(max_length=255)
    password_hash = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now())


class Message(models.Model):
    text = models.CharField(max_length=255)
    author_id = models.ForeignKey(
        User,
        related_name='messages',
        on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(default=timezone.now())
