from django.db import models
from django.utils import timezone
from userfrontend.models import userregisterdb

from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

class Gamedb(models.Model):




    GENRE_CHOICES = [
    ('Action', 'Action'),
    ('Adventure', 'Adventure'),
    ('Role-Playing Game (RPG)', 'Role-Playing Game (RPG)'),
    ('Simulation', 'Simulation'),
    ('Strategy', 'Strategy'),
    ('Sports and Racing', 'Sports and Racing'),
    ('Puzzle', 'Puzzle'),
    ('Platformer', 'Platformer'),
    ('Horror', 'Horror'),
    ('Fighting', 'Fighting'),
    ('Music and Rhythm', 'Music and Rhythm'),
    ('Party and Mini-Games', 'Party and Mini-Games'),
    ('Educational', 'Educational'),
    ('Open World', 'Open World'),
    ('MMORPG (Massively Multiplayer Online Role-Playing Game)', 'MMORPG (Massively Multiplayer Online Role-Playing Game)'),
]
    title = models.CharField(max_length=50)
    shortdesc = models.CharField(max_length=200)

    genres = models.CharField(max_length=100, default="Action",choices=GENRE_CHOICES)

    developer_publisher = models.CharField(max_length=30)
    tags = TaggableManager()
    platforms = models.CharField(max_length=100, default="Unknown")
    cover_art = models.ImageField(upload_to='covers/')
    release_date = models.DateTimeField(default=timezone.now)
    description = RichTextField() 
    views = models.IntegerField(default=0)
    
    
    
    
    def __str__(self):
     return "%s %s"%(self.title,self.developer_publisher)
    
    
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField() 
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    

from django.contrib.auth.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to the User model
    gamedb = models.ForeignKey(Gamedb, on_delete=models.CASCADE)  # ForeignKey to the Gamedb model
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.message
