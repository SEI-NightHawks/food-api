from django.urls import path
from .views import CreateUserView, LoginView, UserProfileUpdateView, VerifyUserView, UserPostList, PostList, PostDetail, PostCommentList, CommentList, CommentDetail, CommentDelete

urlpatterns = [
  # User routes
  path('users/register/', CreateUserView.as_view(), name='register'),
  path('users/login/', LoginView.as_view(), name='login'),
  path('users/verify/', VerifyUserView.as_view(), name='verify_user'),

  path('user/profile/', UserProfileUpdateView.as_view(), name='user-profile-update'),

  # User Posts routes
  path('user/posts/<int:user_profile_id>/', UserPostList.as_view(), name='user-post-list'),

  # Post routes
  path('posts/', PostList.as_view(), name='post-list'),  # List all posts and create a post
  path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),  # Retrieve, update, and delete a specific post

  # Comment routes
  path('comments/', CommentList.as_view(), name='comment-list'),  # List all comments and create a comment
  path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),  # Update and delete a specific comment
  path('posts/<int:post_id>/comments/', PostCommentList.as_view(), name='post-comment-list'), # Shows comments based on that specific post
  path('comments/<int:pk>/delete/', CommentDelete.as_view(), name='comment-delete'),

]

# Like routes??