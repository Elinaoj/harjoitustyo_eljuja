from django.contrib import admin
from .models import Artikkeli, Aika, Myynti, Taloyhtio, Asunto

# Register your models here.

admin.site.register(Artikkeli)
admin.site.register(Aika)
admin.site.register(Myynti)
admin.site.register(Taloyhtio)
admin.site.register(Asunto)
