from django import forms
from . import models
from django.forms import ModelForm

class CreateArtikkeli(forms.ModelForm):
    class Meta:
        model = models.Artikkeli
        prefix = 'artikkeli'
        fields = ['artikkeli', 'hinta', 'lisatietoja']

class CreateKpl(CreateArtikkeli):
    class Meta:
        model = models.Kpl
        prefix = 'kpl'
        fields = ['kpl']
    
#class CreateAika(CreateArtikkeli):
#    class Meta:
#        models = models.Aika
#        prefix = 'aika'
#        fields = ['16.30', '17.00', '17.30', '18.00']
        #fields = (['AIKA1', 'AIKA2', 'AIKA3', 'AIKA4'])

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

