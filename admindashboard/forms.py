# forms.py
from django import forms
from .models import Gamedb


    

class GameForm(forms.ModelForm):
    class Meta:
        model = Gamedb
        fields = ['title', 'developer_publisher', 'cover_art', 'release_date', 'description', 'genres', 'tags', 'platforms']
