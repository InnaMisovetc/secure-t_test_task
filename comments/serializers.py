from rest_framework.serializers import ModelSerializer
from .models import Comment
from rest_framework import serializers


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentSerializer(ModelSerializer):
    replies = RecursiveSerializer(many=True, read_only=True)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'post', 'parent', 'updated_at', 'replies']
        extra_kwargs = {'id': {'read_only': True}}

    def validate(self, data):
        if data['parent']:
            if data['parent'].post != data['post']:
                raise serializers.ValidationError('The parent comment you want to comment has another post number')
        return data



