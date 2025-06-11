from django import forms
from . import models
from django.forms import ModelForm
from .models import Aika

class CreateArtikkeli(forms.ModelForm):
    class Meta:
        model = models.Artikkeli
        prefix = 'artikkeli'
        fields = ['artikkeli', 'hinta', 'lisatietoja']

class AikaForm(forms.Form):
    aika = forms.ModelChoiceField(
        queryset=Aika.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None,
        )

class AsuntoForm(forms.ModelForm):
    class Meta:
        model = models.Asunto
        fields = ['nimi', 'taloyhtio']
