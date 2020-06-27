from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Post, Comment, Author
from .forms import CommentForm, PostForm

def index(request):
    return render(request, 'index.html',{})

def get_author(user):
    get_data = Author.objects.filter(user=user)
    if get_data.exists():
        return get_data[0]
    return None

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

def blog_detail(request, slug):
    #post = Post.objects.get(id=id)
    #post = get_object_or_404(Post, id=id)
    post = get_object_or_404(Post, slug=slug)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author_comment=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form
    }
    return render(request, "blog-detail.html", context)

def blog_update(request, id):
    editor_title="Update"
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("blog-detail-page", kwargs={
                'slug': form.instance.slug
            }))

    context = {
        "form": form,
        "editor_title": editor_title
    }
    return render(request, "blog-create.html", context)

def blog_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect(reverse("blog-list-page"))

def blog_create(request):
    editor_title = "Create"
    form = PostForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("blog-detail-page", kwargs={
                'slug': form.instance.slug
            }))

    context = {
        "form": form,
        "editor_title":editor_title
    }
    return render(request, "blog-create.html", context)
