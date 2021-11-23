from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsAuthorOrReadOnly


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
    lookup_field = 'id'
