from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


# Create your models here.

class Artikkeli(models.Model):
    artikkeli = models.CharField(max_length=75)
    hinta = models.DecimalField(default=0, decimal_places=2, max_digits=4)
    lisatietoja = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artikkeli
    
    class Meta:
        verbose_name_plural = 'Artikkelit'


class Aika(models.Model):
    aika = models.CharField(max_length=5, unique=True) 

    def __str__(self):
        return self.aika   

    class Meta:
        verbose_name_plural = 'Ruoka-ajat'


class Taloyhtio(models.Model):
    taloyhtio = models.CharField(max_length=120, unique=True, blank=False, null=False)
    
    def __str__(self):
        return self.taloyhtio

    class Meta:
        verbose_name_plural = 'Taloyhtiot'

class Asunto(models.Model):
    asunto = models.CharField(max_length=6, blank=False, null=False)
    taloyhtio = models.ForeignKey(Taloyhtio, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.asunto  

    class Meta:
        verbose_name_plural = 'Asunnot'

class Myynti(models.Model):
    artikkeli = models.ForeignKey(Artikkeli, on_delete=models.CASCADE, blank=False)
    kpl = models.IntegerField(blank=True)
    aika = models.ForeignKey(Aika, on_delete=models.CASCADE, null=True, blank=True)
    taloyhtio = models.ForeignKey(Taloyhtio, on_delete=models.CASCADE, null=True, blank=True)
    asunto = models.ForeignKey(Asunto, on_delete=models.CASCADE, null=True, blank=True)
    
    # def __str__(self):
    #     return self.artikkeli
    
    class Meta:
        verbose_name_plural = 'Myynnit'
    

    
   