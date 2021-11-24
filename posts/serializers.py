from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from comments.models import Comment
from comments.serializers import CommentSerializer
from posts.models import Post


class PostSerializer(ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['post_id', 'title', 'content', 'author', 'updated_at', 'comments']
        extra_kwargs = {'id': {'read_only': True}}

    def get_comments(self, obj):
        queryset = Comment.objects.filter(post_id=obj.post_id, parent_id=None)
        serializer = CommentSerializer(queryset, many=True)
        return serializer.data
