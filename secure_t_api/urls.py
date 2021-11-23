from django.contrib import admin
from django.urls import path, include
from comments.views import CommentCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('users/', include('users.urls')),
    path('comments/', CommentCreateView.as_view()),
]
