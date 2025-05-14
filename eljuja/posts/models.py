from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


# Create your models here.

class Post(models.Model):
    #Tähän artikkelityypin valinta (liput, juomat) ja artikkeli_id, jolla voidaan järjestää artikkelit fiksusti
    artikkeli = models.CharField(max_length=75)
    hinta = models.FloatField(default=0)
    lisatietoja = models.CharField()

    def __str__(self):
            return self.artikkeli

#class Node(models.Model):
    #artikkeli_id = models.CharField(primary_key=True)
#    artikkeli = models.CharField(max_length=75)
#    hinta = models.FloatField(default=0)
#    lisatietoja = models.CharField()

class Kpl(models.Model):
    kpl = models.IntegerField()  

    def __str__(self):
        return self.kpl

# class TaloyhtiotModel(models.Model):
#     TALOYHTIO_CHOICES = {'AATELITIE_3': 'Aatelitie_3', 'AATELITIE_5_7': 'Aatelitie_5_7', 'AATELISHERRA': 'Aatelisherra', 'AATELISROUVA': 'Aatelisrouva', 'RENKIPOIKA': 'Renkipoika', 'PIIKATYTTO': 'Piikatytto', 'OMAKOTITALOT': 'Omakotitalot'}
#     name = 'Taloyhtiö'
#     taloyhtio = models.CharField(max_length=30, choices=TALOYHTIO_CHOICES)


class Taloyhtio(models.Model):
     name = models.CharField(max_length=128)


class Asunto(models.Model):
    name = models.CharField(max_length=128)
    taloyhtio = models.ForeignKey(Taloyhtio, on_delete=models.CASCADE, related_name='asunnot')

    


class aika(models.Model):
    AIKA1 = '16.30'
    AIKA2 = '17.00'
    AIKA3 = '17.30'
    AIKA4 = '18.00'
    AIKA_CHOICES = {
    AIKA1: '16.30',
    AIKA2: '17.00',
    AIKA3: '17.30',
    AIKA4: '18.00'
    }
    aika = models.CharField(max_length=5, choices=AIKA_CHOICES, default=AIKA1)

    def __str__(self):
         return self.aika
    


   
    
   