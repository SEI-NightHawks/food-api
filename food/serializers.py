from rest_framework import serializers
# renders into json for us.
from .models import Post, Comment, Like, UserProfile, User

class UserSerializer(serializers.ModelSerializer):
    profile_pic_url = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'profile_pic_url']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        profile_pic_url = validated_data.pop('profile_pic_url', None)
        user = User.objects.create_user(**validated_data)
        
        # Create UserProfile for the new user with profile_pic_url
        profile = UserProfile.objects.create(user=user)
        if profile_pic_url:
            profile.profile_pic_url = profile_pic_url
            profile.save()

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

    post_likes = serializers.PrimaryKeyRelatedField(
        many=True, 
        queryset=UserProfile.objects.all(),
        required=False  # This makes the field optional
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
    user_profile = serializers.PrimaryKeyRelatedField(
        queryset=UserProfile.objects.all(),
        write_only=True
        
    )

    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(),
        write_only=True
    )


    def to_representation(self, instance):
        representation = super(CommentSerializer, self).to_representation(instance)
        representation['user_profile'] = UserProfileSerializer(instance.user_profile).data
        representation['post'] = PostSerializer(instance.post).data
        return representation

    class Meta:
        model = Comment
        fields = '__all__'


# class CreateCommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ['post', 'comment']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
