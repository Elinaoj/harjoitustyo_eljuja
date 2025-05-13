#from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post
from posts.models import Taloyhtio, Asunto

#def register(request):
#    return render(request, 'register.html')

def homepage(request):
    #return HttpResponse('Pääsivu')
    return render(request, 'home.html')

def myynti(request):
    # return HttpResponse('Myynti')
    posts = Post.objects.all()

    return render(request, 'myynti.html', { 'posts': posts })

def taloyhtio(request):
    taloyhtiot = ["Aatelitie_3", "Aatelitie_5_7", "Aatelisherra", "Aatelisrouva", "Renkipoika", "Piikatytto", "Omakotitalot"]
    return render (request, 'myynti.html', { 'taloyhtiot', taloyhtiot })

def taloyhtiot(request):
    taloyhtiot = Taloyhtio.object.all()
    context = {'taloyhtiot': taloyhtiot}
    return render(request, 'myynti.html', context)