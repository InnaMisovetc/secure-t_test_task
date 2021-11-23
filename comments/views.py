from rest_framework.generics import CreateAPIView
from .models import Comment
from .serializers import CommentSerializer


class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    model = Comment
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
