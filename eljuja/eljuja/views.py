#from django.http import HttpResponse
from django.shortcuts import render
from artikkelit.models import Artikkeli
from artikkelit.models import Taloyhtio, Asunto
from django.contrib.auth.decorators import login_required


#def register(request):
#    return render(request, 'register.html')

def homepage(request):
    #return HttpResponse('Pääsivu')
    return render(request, 'home.html')

@login_required
def myynti(request):
    # return HttpResponse('Myynti')
    artikkelit = Artikkeli.objects.all()

    return render(request, 'myynti.html', { 'artikkelit': artikkelit })

def taloyhtio(request):
    taloyhtiot = ["Aatelitie_3", "Aatelitie_5_7", "Aatelisherra", "Aatelisrouva", "Renkipoika", "Piikatytto", "Omakotitalot"]
    return render (request, 'myynti.html', { 'taloyhtiot', taloyhtiot })

def taloyhtiot(request):
    taloyhtiot = Taloyhtio.object.all()
    context = {'taloyhtiot': taloyhtiot}
    return render(request, 'myynti.html', context)