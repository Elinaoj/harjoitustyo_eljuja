from django import forms
from . import models
from django.forms import ModelForm

class CreateArtikkeli(forms.ModelForm):
    class Meta:
        model = models.Artikkeli
        prefix = 'artikkeli'
        fields = ['artikkeli', 'hinta', 'lisatietoja']

class AikaForm(forms.ModelForm):
    class Meta:
        model = models.Aika
        fields = ['aika']
        widgets = {
            'aika': forms.RadioSelect(choices=[
                ('16.30', '16.30'),
                ('17.00', '17.00'),
                ('17.30', '17.30'),
                ('18.00', '18.00'),
            ])
        }
    # aika = forms.ChoiceField(choices=aika_valinta, widget=forms.RadioSelect)

class MyyntiForm(forms.ModelForm):
    class Meta:
        model = models.Myynti
        fields = ['artikkeli', 'kpl']