from django.urls import path
from .views import CreateUserView, LoginView, UserProfileUpdateView, UserPostList, PostList, PostDetail, CommentList, CommentDetail

urlpatterns = [
  # User routes
  path('users/register/', CreateUserView.as_view(), name='register'),
  path('users/login/', LoginView.as_view(), name='login'),
  path('user/profile/', UserProfileUpdateView.as_view(), name='user-profile-update'),

  # User Posts routes
  path('user/posts/<int:user_profile_id>/', UserPostList.as_view(), name='user-post-list'),

  # Post routes
  path('posts/', PostList.as_view(), name='post-list'),  # List all posts and create a post
  path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),  # Retrieve, update, and delete a specific post

  # Comment routes
  path('comments/', CommentList.as_view(), name='comment-list'),  # List all comments and create a comment
  path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),  # Update and delete a specific comment
]

# Like routes??