from django.urls import path
from .views import CreateUserView, LoginView, PostList, PostDetail, CommentList, CommentDetail, LikeViewSet

urlpatterns = [
  # User routes
  path('users/register/', CreateUserView.as_view(), name='register'),
  path('users/login/', LoginView.as_view(), name='login'),

  # Post routes
  path('posts/', PostList.as_view(), name='post-list'),  # List all posts and create a post
  path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),  # Retrieve, update, and delete a specific post

  # Comment routes
  path('comments/', CommentList.as_view(), name='comment-list'),  # List all comments and create a comment
  path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),  # Update and delete a specific comment
]

# Like routes??