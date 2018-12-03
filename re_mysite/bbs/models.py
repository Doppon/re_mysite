from django.db import models

class Topic(models.Model):
    title = models.CharField(max_length=100)


class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
