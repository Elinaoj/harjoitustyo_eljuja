from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


# Create your models here.

class Post(models.Model):
    artikkeli_id = models.CharField(primary_key=True)
    artikkeli = models.CharField(max_length=75)
    hinta = models.FloatField(default=0)
    lisatietoja = models.CharField()

    def __str__(self):
            return self.artikkeli

    
    
    
    
    


   
    
   