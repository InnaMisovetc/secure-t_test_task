from rest_framework import status
from rest_framework.generics import ListCreateAPIView, get_object_or_404
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from secure_t_api.permissions import IsAuthorOrReadOnly
from .models import Comment
from .serializers import CommentSerializer
from posts.models import Post


class CommentListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Comment.objects.all()
    model = Comment
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        post = Post.objects.get(post_id=post_id)
        serializer.save(author=self.request.user, post=post)


class CommentDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]

    queryset = Comment.objects.all()
    model = Comment
    serializer_class = CommentSerializer
    lookup_field = 'comment_id'

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.content = 'Comment was deleted.'
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
