#from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post

def homepage(request):
    #return HttpResponse('Pääsivu')
    return render(request, 'home.html')

def myynti(request):
    # return HttpResponse('Myynti')
    posts = Post.objects.all().order_by('-date')
    return render(request, 'myynti.html', { 'posts': posts })

#def register(request):
#    return render(request, 'register.html')