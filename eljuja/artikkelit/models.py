from django.db import models

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
    nimi = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nimi
    
    class Meta:
        verbose_name_plural = 'Taloyhtiot'
        managed = True

class Asunto(models.Model):
    nimi = models.CharField(max_length=5, blank=True)
    taloyhtio = models.ForeignKey(Taloyhtio, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.nimi
    
    class Meta:
        verbose_name_plural = 'Asunnot'
        managed = True

   
class Myynti(models.Model):
    artikkeli = models.ForeignKey(Artikkeli, on_delete=models.CASCADE)
    kpl = models.IntegerField(blank=True)
    aika = models.ForeignKey(Aika, on_delete=models.CASCADE, null=True, blank=True)
    taloyhtio = models.ForeignKey(Taloyhtio, on_delete=models.CASCADE, null=True, blank=True)
    asunto = models.ForeignKey(Asunto, on_delete=models.CASCADE, null=True, blank=True)
    kateismyynti = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Myynnit'
        managed = True

       
   