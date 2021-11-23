from django.urls import path
from .views import PostListCreateView, PostDetailView

urlpatterns = [
    path('', PostListCreateView.as_view()),
    path('<id>/', PostDetailView.as_view())
]
