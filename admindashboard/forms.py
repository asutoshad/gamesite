# forms.py
from django import forms
from .models import Gamedb
from .models import BlogPost


    

class GameForm(forms.ModelForm):
    class Meta:
        model = Gamedb
        fields = ['title','shortdesc', 'developer_publisher', 'cover_art', 'release_date', 'description', 'genres', 'tags', 'platforms','views']


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','content', 'pub_date', 'views']




