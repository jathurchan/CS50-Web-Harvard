from django.contrib.auth.models import AbstractUser
from django.db import models

import uuid


class User(AbstractUser):
    following = models.ManyToManyField("self", blank=True, symmetrical=False, related_name="followers")

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # each post uniquely identified using UUID v4
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="posts")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # Automatically set the field to now when the post is created
    likes = models.ManyToManyField(User, blank=True, related_name="liked")

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user.username,
            "text": self.text,
            "created_at": self.created_at.strftime("%b %d %Y, %I:%M %p"),
            "likes": [user.username for user in self.likes.all()],
        }