from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from posts.models import Post
from comments.models import Comment
from comments.serializers import CommentSerializer


class PostSerializer(ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'updated_at', 'comments']

    def get_comments(self, obj):
        queryset = Comment.objects.filter(post_id=obj.id, parent_id=None)
        serializer = CommentSerializer(queryset, many=True)
        return serializer.data

