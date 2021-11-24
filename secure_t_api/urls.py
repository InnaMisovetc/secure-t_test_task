from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

from users.views import UserCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('users/', include('users.urls')),
    path('comments/', include('comments.urls')),
    path('register/', UserCreateView.as_view()),
    path('login/', views.obtain_auth_token),
]
