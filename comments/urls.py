from django.urls import path

from .views import CommentListCreateView, CommentDetailView

urlpatterns = [
    path('', CommentListCreateView.as_view()),
    path('<comment_id>/', CommentDetailView.as_view())
]
