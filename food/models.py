from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic_url = models.URLField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.user.username

class Post(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    post_likes = models.ManyToManyField(UserProfile, related_name='liked_posts')

    def __str__(self):
        return self.user_profile.user.username

class Like(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    liked_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return self.user_profile.user.username

class Comment(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    def __str__(self):
        return self.user_profile.user.username