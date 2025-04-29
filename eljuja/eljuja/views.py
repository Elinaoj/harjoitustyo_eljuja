#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse('Pääsivu')
    return render(request, 'home.html')

def myynti(request):
    # return HttpResponse('Myynti')
    return render(request, 'myynti.html')

#def register(request):
#    return render(request, 'register.html')