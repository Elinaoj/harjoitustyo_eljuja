from django import forms
from . import models
from django.forms import ModelForm
from .models import Taloyhtio, Asunto

class CreateArtikkeli(models.ModelForm):
    class Meta:
        model = models.Artikkeli
        prefix = 'artikkeli'
        fields = ['artikkeli', 'hinta', 'lisatietoja']

class AikaForm(models.ModelForm):
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


class AsuntoForm(forms.ModelForm):
    class Meta:
        model = models.Asunto
        fields = ['taloyhtio', 'asunto']
        labels = {
            'taloyhtio': 'taloyhtio',
            'asunto': 'asunto'
        }

        widgets = {
            'taloyhtio': forms.Select(attrs={'onchange': 'get_asunto_by_taloyhtio(this.value);'})
        }

class MyyntiForm(models.ModelForm):
    class Meta:
        model = models.Myynti
        fields=('artikkeli', 'kpl', 'taloyhtio', 'asunto')
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['asunto'].queryset = Asunto.objects.none()

        if 'taloyhtio' in self.data:
            try:
                taloyhtio_id = int(self.data.get('taloyhtio'))
                self.fields['asunto'].queryset = Asunto.objects.filter(taloyhtio_id=taloyhtio_id).order_by('asunto')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['asunto'].queryset = self.instance.taloyhtio.asunto_set.order_by('asunto')    
