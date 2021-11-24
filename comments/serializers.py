from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Comment


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentSerializer(ModelSerializer):
    replies = RecursiveSerializer(many=True, read_only=True)
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.ReadOnlyField(source='post.post_id')

    class Meta:
        model = Comment
        fields = ['comment_id', 'author', 'content', 'post', 'parent', 'updated_at', 'replies']
        extra_kwargs = {'comment_id': {'read_only': True}}

    def update(self, instance, validated_data):
        if validated_data['post'] != instance.post:
            raise serializers.ValidationError('You must not change post id.')
        if validated_data['parent'] != instance.parent:
            raise serializers.ValidationError('You must not change parent comment id.')
        return super().update(instance, validated_data)
