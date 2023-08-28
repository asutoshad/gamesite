from django.db import models
from django.utils import timezone


class Gamedb(models.Model):
    title = models.CharField(max_length=5)
    genres = models.CharField(max_length=100, default="Unknown")
    developer_publisher = models.CharField(max_length=30)
    tags = models.CharField(max_length=100, default="Unknown")
    platforms = models.CharField(max_length=100, default="Unknown")
    cover_art = models.ImageField(upload_to='covers/')
    release_date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=50)
    
    
    
    
    def __str__(self):
     return "%s %s"%(self.title,self.developer_publisher)