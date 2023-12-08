from rest_framework import serializers
# renders into json for us.
from .models import Post, Comment, Like, UserProfile, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user)  # Create UserProfile for the new user
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    # Use PrimaryKeyRelatedField for write operations
    user_profile = serializers.PrimaryKeyRelatedField(
        queryset=UserProfile.objects.all(),
        write_only=True
    )

    # Override to_representation to control read operations
    def to_representation(self, instance):
        representation = super(PostSerializer, self).to_representation(instance)
        representation['user_profile'] = UserProfileSerializer(instance.user_profile).data
        return representation

    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
