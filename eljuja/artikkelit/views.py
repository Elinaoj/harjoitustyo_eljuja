from django.shortcuts import render, redirect
from .models import Artikkeli
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.


def artikkelit_lista(request):
    artikkelit = Artikkeli.objects.all()
    return render(request, 'artikkelit/artikkelit_lista.html', {'artikkelit': artikkelit})


def artikkeli_page(request):
    artikkelit = Artikkeli.objects.all()
    return render(request, 'artikkelit/artikkeli_sivu.html', {'artikkelit': artikkelit})

def artikkeli_uusi(request):     
    artikkelit = Artikkeli.objects.all()
    return render (request, 'artikkelit/artikkeli_uusi.html', { 'artikkelit': artikkelit })

@login_required
def artikkeli_uusi(request):
    if request.method == 'POST': 
        form = forms.CreateArtikkeli(request.POST, request.FILES) 
        if form.is_valid():
            newartikkeli = form.save(commit=False) 
            newartikkeli.author = request.user 
            newartikkeli.save()
            return  render(request, 'artikkelit/artikkeli_uusi.html', { 'form': form })
    else:
        form = forms.CreateArtikkeli()
    return render(request, 'artikkelit/artikkeli_uusi.html', { 'form': form })

#def aika(request):
#    ajat = [
#        '16.30', '17.00', '17.30', '18.00'
#    ]
#    context = {'ajat': ajat}
#    return render(request, 'myynti.html', context)