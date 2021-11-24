from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from comments.models import Comment
from comments.serializers import CommentSerializer
from secure_t_api.permissions import IsActiveUserOrReadOnly
from .models import User
from .serializers import UserSerializer


class UserListView(ListAPIView):
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateView(CreateAPIView):
    permission_classes = [AllowAny]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsActiveUserOrReadOnly]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
