from django.urls import path
from .views import UserListView, UserCreateView
from rest_framework.authtoken import views

urlpatterns = [
    path('', UserListView.as_view()),
    path('register/', UserCreateView.as_view()),
    path('login/', views.obtain_auth_token)
]
