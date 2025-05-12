from django import forms
from . import models
from django.forms import ModelForm

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        prefix = 'post'
        fields = ['artikkeli', 'hinta', 'lisatietoja']

class CreateKpl(CreatePost):
    class Meta:
        model = models.Kpl
        prefix = 'kpl'
        fields = ['kpl']
    
class CreateAika(CreatePost):
    class Meta:
        models = models.aika
        prefix = 'aika'
        #fields = ['16.30', '17.00', '17.30', '18.00']
        fields = (['AIKA1', 'AIKA2', 'AIKA3', 'AIKA4'])