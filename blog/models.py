from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Blog(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=800, blank=True, null=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(default=timezone.now) 
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    
    def __str__(self):
        return self.title