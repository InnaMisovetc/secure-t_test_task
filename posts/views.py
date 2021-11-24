from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from secure_t_api.permissions import IsAuthorOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'post_id'
