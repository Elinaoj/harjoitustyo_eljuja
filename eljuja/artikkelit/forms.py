from django import forms
from . import models
from django.forms import ModelForm

class CreateArtikkeli(forms.ModelForm):
    class Meta:
        model = models.Artikkeli
        prefix = 'artikkeli'
        fields = ['artikkeli', 'hinta', 'lisatietoja']

    # aika = forms.ChoiceField(choices=aika_valinta, widget=forms.RadioSelect)

class AikaForm(forms.ModelForm):
    class Meta:
        model = models.Aika
        fields = ['aika']
        widgets = {
            'aika': forms.RadioSelect(choices=[
                ('1630', '1630'),
                ('1700', '1700'),
                ('1730', '1730'),
                ('1800', '1800'),
            ])
        }

class MyyntiForm(forms.ModelForm):
    class Meta:
        model = models.Myynti
        fields = ['artikkeli', 'kpl', 'aika', 'taloyhtio', 'asunto']

class AsuntoForm(forms.ModelForm):
    class Meta:
        model = models.Asunto
        fields = ['nimi', 'taloyhtio']
