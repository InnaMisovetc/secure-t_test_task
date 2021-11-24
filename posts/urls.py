from django.urls import path, include

from .views import PostListCreateView, PostDetailView
from comments.views import CommentCreateView, CommentDetailView

urlpatterns = [
    path('', PostListCreateView.as_view()),
    path('<post_id>/', PostDetailView.as_view()),
    path('comments/', include('comments.urls')),
]
