from django.shortcuts import render
from posts.models import Post

# Create your views here.

def myytavat(request):
    posts = Post.objects.all()
    return render(request, 'myytavat/myytavat.html', {'posts': posts})

