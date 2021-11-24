import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    id = models.CharField(max_length=100, unique=True, blank=True, default=uuid.uuid4, primary_key=True, name='post_id')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
