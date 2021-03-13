from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    dislikes = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.content
