from django.shortcuts import render, get_object_or_404
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

def blog_detail(request, id):
    #post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)

    '''form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)'''
    context = {
        "post": post,
        #"comments": comments,
        #"form": form,
    }
    return render(request, "blog-detail.html", context)
