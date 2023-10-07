# forms.py
from django import forms
from .models import Gamedb
from .models import BlogPost, Comment


    

class GameForm(forms.ModelForm):
    class Meta:
        model = Gamedb
        fields = ['title','shortdesc', 'developer_publisher', 'cover_art', 'release_date', 'description', 'genres', 'tags', 'platforms','views']


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','content', 'pub_date', 'views']




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
        # Define fields and widgets as needed

    user = forms.CharField(widget=forms.HiddenInput())
    gamedb = forms.CharField(widget=forms.HiddenInput())
