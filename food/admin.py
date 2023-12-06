from django.contrib import admin
from .models import UserProfile, Post, Like, Comment

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)

# Register your models here.