from django.contrib import admin
from .models import Artikkeli, Aika, Myynti

# Register your models here.

admin.site.register(Artikkeli)
admin.site.register(Aika)
admin.site.register(Myynti)
