from django import forms
from . import models
from django.forms import ModelForm

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['artikkeli_id', 'artikkeli', 'hinta', 'lisatietoja']


    
