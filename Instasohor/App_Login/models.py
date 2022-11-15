from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    new_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    f_name = models.CharField(max_length=50, blank=True)
    l_name = models.CharField(max_length=50, blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)
    dob = models.DateField(blank=True, null=True)
    about = models.TextField(blank=True)
    website_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
