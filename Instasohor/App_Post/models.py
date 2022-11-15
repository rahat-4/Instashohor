from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user_post = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_post")
    image = models.ImageField(upload_to="post_images")
    caption = models.CharField(max_length=200, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-upload_date']

class Like(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liker")
    liked_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="liked_post")
