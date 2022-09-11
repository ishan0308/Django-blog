from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect
from blog.models import BlogPost
from blog.forms import BlogPostForm

def archive(request):
    posts = BlogPost.objects.all()[:30]
    return render(request, 'archive.html',{'form': BlogPostForm(request.POST or None)})

def display_blogs(request):
    posts = BlogPost.objects.all()[:30]
    return render(request, 'display.html',{'posts': posts, 'form': BlogPostForm(request.POST or None)})

def create_blogpost(request):
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.timestamp=datetime.now()
        post.save()
        return HttpResponseRedirect('/blog/display')
    else:
        return HttpResponseRedirect('/blog/')

