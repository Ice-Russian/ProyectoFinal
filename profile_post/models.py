from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    content = models.TextField()
    media = models.FileField(upload_to='post/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content[:20]