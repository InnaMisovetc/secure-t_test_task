from django.urls import path, include

from .views import PostListCreateView, PostDetailView

urlpatterns = [
    path('', PostListCreateView.as_view()),
    path('<post_id>/', PostDetailView.as_view()),
    path('<post_id>/comments/', include('comments.urls')),
]
