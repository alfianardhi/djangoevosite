from django.shortcuts import render
from .models import Post

def index(request):
    return render(request, 'index.html',{})

def about(request):
    return render(request, 'about.html',{})

def termnco(request):
    return render(request, 'terms-conditions.html',{})

def privacy(request):
    return render(request, 'privacy-policy.html',{})

def blog(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts':posts
    }
    return render(request, 'blog.html',context)
