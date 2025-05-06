from django import forms
from . import models
from posts.models import Post


class LuoMyynti(forms.ModelForm):
    class Meta:
        model = models.eljuja
        fields = ['Post.artikkeli_id', 'hinta', 'kpl']


#class CreatePost(forms.ModelForm):
#    class Meta:
#        model = models.Post
#        fields = ['artikkeli_id', 'artikkeli', 'hinta', 'lisatietoja']

#class Taloyhtiot(forms.ModelForm):
#    class Meta:
 #       model = models.Post
#        fields = ["Aatelitie_3", "Aatelitie_5_7", "Aatelisherra", "Aatelisrouva", "Renkipoika", "Piikatytto", "Omakotitalot"]
