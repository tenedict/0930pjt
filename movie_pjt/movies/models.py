from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cnt = models.IntegerField(default=0)
    star = models.CharField(max_length=20,default='⭐⭐⭐')