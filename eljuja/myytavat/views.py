from django.shortcuts import render
from posts.models import Post
from .models import Myytava
from . import forms

# Create your views here.

def myytavat(request):
    posts = Post.objects.all()
    return render(request, 'myytavat/myytavat.html', {'myytavat': myytavat})

