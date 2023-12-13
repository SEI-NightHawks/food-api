from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import generics, permissions, status, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import UserProfile, Post, Comment, Like
from .serializers import UserProfileSerializer, PostSerializer, CommentSerializer, LikeSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# User Registration
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        user_profile = UserProfile.objects.get(user=user, profile_pic_url=response.data['profile_pic_url'])
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_profile': UserProfileSerializer(user_profile).data
        })

# User Login
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            user_profile = UserProfile.objects.get(user=user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_profile': UserProfileSerializer(user_profile).data
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserProfileUpdateView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Fetch the user profile of the currently authenticated user
        return self.request.user.userprofile


class VerifyUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user)  # Fetch user profile
        refresh = RefreshToken.for_user(request.user)  # Generate new refresh token
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_profile': UserProfileSerializer(user_profile).data
        })


class UserPostList(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        # Get the user_profile_id from the URL
        user_profile_id = self.kwargs['user_profile_id']
        # Filter the posts by the user_profile_id
        return Post.objects.filter(user_profile=user_profile_id)

# Post Views (with protected POST route; requires token in header)
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # Define permission classes based on action
    def get_permissions(self):
        if self.request.method == 'POST':
            # Require authentication for POST requests 
            permission_classes = [IsAuthenticated]
        else:
            # Allow any access for GET requests (blog listing)
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    # Override the perform_create method to set the username as the user's profile
    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user.userprofile)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Comment Views
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # Override the perform_create method to set the author as the user's profile:
    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user.userprofile)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class PostCommentList(generics.ListAPIView):
    serializer_class = CommentSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at']  # You can adjust the ordering based on your needs
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post=post_id)


class CommentDelete(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.user_profile.user != self.request.user:
            raise PermissionDenied("You do not have permission to delete this comment.")
        instance.delete()
#Like Views
class LikeViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


# from rest_framework import viewsets
# from .serializers import PostSerializer, CommentSerializer, UserProfileSerializer, LikeSerializer
# from .models import Post, Comment, UserProfile, Like

# # Create your views here.

# class UserProfileViewSet(viewsets.ModelViewSet):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
