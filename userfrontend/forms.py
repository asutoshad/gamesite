from django import forms
from .models import userregisterdb


class userregister(forms.ModelForm):
    class Meta:
        model = userregisterdb
        fields = ['email','username','gender','password']
