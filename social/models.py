from django.conf import settings
from django.db import models
from django.utils import timezone

# Choices for theme
THEME_CHOICES = [
    ('default', 'Default'),
    ('dark', 'Dark'),
    ('light', 'Light'),
]

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    
    theme = models.CharField(max_length=10, choices=THEME_CHOICES, default='default')
    
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
    website = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    
    join_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
