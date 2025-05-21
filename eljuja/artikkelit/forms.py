from django import forms
from . import models
from django.forms import ModelForm

class CreateArtikkeli(forms.ModelForm):
    class Meta:
        model = models.Artikkeli
        prefix = 'artikkeli'
        fields = ['artikkeli', 'hinta', 'lisatietoja']

    
class AikaForm(forms.Form):
    aika_valinta = [
        ('1', '16.30'),
        ('2', '17.00'),
        ('3', '17.30'),
        ('4', '18.00'),
    ]
  
    aika = forms.ChoiceField(choices=aika_valinta, widget=forms.RadioSelect)

class MyyntiForm(forms.ModelForm):
    class Meta:
        model = models.Myynti
        fields = ['artikkeli', 'kpl', 'alle_3v', 'taloyhtio', 'asunto', 'maidoton', 'gluteeniton', 'kasvis', 'vegaaninen', 'extra_burger']