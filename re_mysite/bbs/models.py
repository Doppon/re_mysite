from django.db import models
from django.utils import timezone

class Topic(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField('登録日時', default=timezone.now)


class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField('登録日時', default=timezone.now)
