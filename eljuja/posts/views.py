from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts_list.html', {'posts': posts})


def post_page(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_page.html', {'posts': posts})

# def post_new(request):
#     posts = Post.objects.all()
#     return render (request, 'posts/post_new.html', { 'posts': posts })

@login_required
def post_new(request):
    if request.method == 'POST': 
        form = forms.CreatePost(request.POST, request.FILES) 
        if form.is_valid():
            newpost = form.save(commit=False) 
            newpost.author = request.user 
            newpost.save()
            return  render(request, 'posts/post_new.html', { 'form': form })
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', { 'form': form })

