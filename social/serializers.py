from rest_framework import serializers
from .models import Profile, Post, FriendRequest, Notification, Settings

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'mobile_number', 'theme', 'bio', 'avatar', 'website', 'twitter', 'instagram', 'join_date', 'last_updated']
        read_only_fields = ['join_date', 'last_updated']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user', 'content', 'created_at']
        read_only_fields = ['created_at']

class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ['from_user', 'to_user', 'created_at', 'accepted']
        read_only_fields = ['created_at']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['user', 'message', 'created_at', 'read']
        read_only_fields = ['created_at']

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ['notifications_enabled', 'dark_mode']
