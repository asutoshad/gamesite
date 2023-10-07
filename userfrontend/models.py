from django.db import models

# Create your models here.
from django.db import models





class userregisterdb(models.Model):





    email = models.CharField(max_length=50)
    username = models.CharField(max_length=200)
    gender = models.CharField(max_length=30)    
    password = models.CharField(max_length=100)

    def __str__(self):
     return "%s %s" % (self.email, self.username)



    