from django.shortcuts import render
from posts.models import Post
from .models import Myytava
from . import forms
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def myytavat(request):
    posts = Post.objects.all()
    if request.method == "POST":
        form = forms.CreateMyytava(request.POST)
        if form.is_valid():
            myytava = form.save(commit=False) 
            myytava.author = request.user 
            myytava.save()
            return render(request, 'myytavat/myytavat.html', { 'form': form })
    else:
        form = forms.CreateMyytava()        
    return render(request, 'myytavat/myytavat.html', {'form': form})

#class NodeView(DetailView):
#    model = Node
#    template_name = 'myytavat.html'