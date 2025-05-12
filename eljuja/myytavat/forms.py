from django import forms
from . import models
from posts.models import Post


class CreateMyytava(forms.ModelForm):
    class Meta:
        model = models.Myytava

        fields = ['kpl']


#class CreatePost(forms.ModelForm):
#    class Meta:
#        model = models.Post
#        fields = ['artikkeli_id', 'artikkeli', 'hinta', 'lisatietoja']

#class Taloyhtiot(forms.ModelForm):
#    class Meta:
 #       model = models.Post
#        fields = ["Aatelitie_3", "Aatelitie_5_7", "Aatelisherra", "Aatelisrouva", "Renkipoika", "Piikatytto", "Omakotitalot"]
