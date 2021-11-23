from django.db import models
from django.contrib.auth import get_user_model
import uuid
from posts.models import Post

User = get_user_model()


class Comment(models.Model):
    id = models.CharField(max_length=100, unique=True, blank=True, default=uuid.uuid4, primary_key=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
    parent = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.PROTECT)
    updated_at = models.DateTimeField(auto_now=True)
