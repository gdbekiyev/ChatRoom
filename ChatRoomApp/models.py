from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Message(models.Model):
    sender = models.CharField(max_length=55)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
