from django.db import models
from posts.models import Post
#from django.contrib.auth.models import User

# Create your models here.

# Jos teet muutoksia aja migrations :
# py (tai) python manage.py makemigrations (tähän voi laittaa app, jos ajaa vain yhden app)
# py (tai) python manage.py migrate



class Myytava(models.Model):
    kpl = models.IntegerField(default=0)
    #monivalinta = models.ManyToManyField("app.Model", verbose_name=("16.30", "17.00", "17.30", "18.00"))
#    artikkeli_id = Post.artikkeli_id
    artikkeli = Post.artikkeli
#    hinta = Post.hinta
#    lisatietoja = Post.lisatietoja

    def __str__(self):
        return self.kpl

#TALOYHTIO_CHOICES = (('Aatelitie_3', 'AATELITIE_3'), ('Aatelitie_5_7', 'AATELITIE_5_7'), ('Aatelisherra', 'AATELISHERRA', ('Aatelisrouva', 'AATELISROUVA'), 'Renkipoika', 'RENKIPOIKA'), ('Piikatytto', 'PIIKATYTTO'), ('Omakotitalot', 'OMAKOTITALOT'))

class TaloyhtiotModel(models.Model):
    TALOYHTIO_CHOICES = {'AATELITIE_3': 'Aatelitie_3', 'AATELITIE_5_7': 'Aatelitie_5_7', 'AATELISHERRA': 'Aatelisherra', 'AATELISROUVA': 'Aatelisrouva', 'RENKIPOIKA': 'Renkipoika', 'PIIKATYTTO': 'Piikatytto', 'OMAKOTITALOT': 'Omakotitalot'}
    name = 'Taloyhtiö'
    taloyhtio = models.CharField(max_length=30, choices=TALOYHTIO_CHOICES)


#class Post(models.Model):
#    artikkeli_id = models.AutoField(primary_key=True)
#    artikkeli = models.CharField(max_length=75)
#    hinta = models.FloatField(default=0)
#    lisatietoja = models.CharField()
    #slug = models.SlugField()
    #date = models.DateTimeField(auto_now_add=True)
    #banner = models.ImageField(default='fallback.png', blank=True)
    #author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    

    def __str__(self):
        return self.artikkeli
