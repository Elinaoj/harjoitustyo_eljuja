#from django.http import HttpResponse
from django.shortcuts import render
from artikkelit.models import Artikkeli, Myynti
#from artikkelit.models import Taloyhtio, Asunto
from django.http import HttpResponseForbidden
from artikkelit.forms import AikaForm


#def register(request):
#    return render(request, 'register.html')

def homepage(request):
    #return HttpResponse('Pääsivu')
    return render(request, 'home.html')

def myynti(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("Kirjaudu ensin sisään.")
    if not request.user.is_superuser:
        return HttpResponseForbidden("Sinulla ei ole oikeuksia käyttää tätä sivua.")
    artikkelit = Artikkeli.objects.all()
    myynnit = Myynti.objects.all()

    aika_form = AikaForm(request.POST or None)
    if request.method == 'POST' and aika_form.is_valid():
        aika_form.save()

    return render(request, 'myynti.html', { 'artikkelit': artikkelit, 'aika_form': aika_form})

#def taloyhtio(request):
#    taloyhtiot = ["Aatelitie_3", "Aatelitie_5_7", "Aatelisherra", "Aatelisrouva", "Renkipoika", "Piikatytto", "Omakotitalot"]
#    return render (request, 'myynti.html', { 'taloyhtiot', taloyhtiot })

#def taloyhtiot(request):
#    taloyhtiot = Taloyhtio.object.all()
#    context = {'taloyhtiot': taloyhtiot}
#    return render(request, 'myynti.html', context)