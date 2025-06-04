from django.db import models
from django.contrib.auth.models import User

class Artikkeli(models.Model):
    artikkeli = models.CharField(max_length=75)
    hinta = models.DecimalField(default=0, decimal_places=2, max_digits=4)
    lisatietoja = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.artikkeli
    
    class Meta:
        verbose_name_plural = 'Artikkelit'
        managed = True

class Aika(models.Model):
    aika = models.CharField(unique=True, max_length=5, blank=False) 

    def __str__(self):
        return self.aika   

    class Meta:
        verbose_name_plural = 'Ruoka-ajat'
        managed = True

class Taloyhtio(models.Model):
    taloyhtio = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = 'Taloyhtiot'
        managed = True

class Asunto(models.Model):
    asunto = models.CharField(max_length=5, blank=True)
    taloyhtio = models.ForeignKey(Taloyhtio, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Asunnot'
        managed = True

class Myynti(models.Model):
    artikkeli = models.ForeignKey(Artikkeli, on_delete=models.CASCADE)
    kpl = models.IntegerField(blank=True)
    aika = models.ForeignKey(Aika, on_delete=models.CASCADE, null=True, blank=True)
    taloyhtio = models.ForeignKey(Taloyhtio, on_delete=models.CASCADE, null=True, blank=True)
    asunto = models.ForeignKey(Asunto, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Myynnit'
        managed = True

#class Node(models.Model):
    #artikkeli_id = models.CharField(primary_key=True)
#    artikkeli = models.CharField(max_length=75)
#    hinta = models.FloatField(default=0)
#    lisatietoja = models.CharField()

# class TaloyhtiotModel(models.Model):
#     TALOYHTIO_CHOICES = {'AATELITIE_3': 'Aatelitie_3', 'AATELITIE_5_7': 'Aatelitie_5_7', 'AATELISHERRA': 'Aatelisherra', 'AATELISROUVA': 'Aatelisrouva', 'RENKIPOIKA': 'Renkipoika', 'PIIKATYTTO': 'Piikatytto', 'OMAKOTITALOT': 'Omakotitalot'}
#     name = 'Taloyhtiö'
#     taloyhtio = models.CharField(max_length=30, choices=TALOYHTIO_CHOICES)


#class Taloyhtio(models.Model):
#    name = models.CharField(max_length=128)


#class Asunto(models.Model):
#    name = models.CharField(max_length=128)
#    taloyhtio = models.ForeignKey(Taloyhtio, on_delete=models.CASCADE, related_name='asunnot')



#class aika(models.Model):
#    AIKA1 = '16.30'
#    AIKA2 = '17.00'
#    AIKA3 = '17.30'
#    AIKA4 = '18.00'
#    AIKA_CHOICES = {
#    AIKA1: '16.30',
#    AIKA2: '17.00',
#    AIKA3: '17.30',
#    AIKA4: '18.00'
#    }
#    aika = models.CharField(max_length=5, choices=AIKA_CHOICES, default=AIKA1)

#    def __str__(self):
#         return self.aika
    


   
    
   