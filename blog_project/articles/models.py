from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Article(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    read_time = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title
