from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Post, Comment, Author
from .forms import CommentForm, PostForm
from django.views.generic import View, ListView


def index(request):
    return render(request, 'index.html',{})

class IndexView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'index.html'
        context={}
        return render(request, template_name, context)

def get_author(user):
    get_data = Author.objects.filter(user=user)
    if get_data.exists():
        return get_data[0]
    return None

def about(request):
    return render(request, 'about.html',{})

class AboutView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'about.html'
        context={}
        return render(request, template_name, context)

def termnco(request):
    return render(request, 'terms-conditions.html',{})

class TermncoView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'terms-conditions.html'
        context={}
        return render(request, template_name, context)

def privacy(request):
    return render(request, 'privacy-policy.html',{})

class PrivacyView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'privacy-policy.html'
        context={}
        return render(request, template_name, context)

def blog(request):
    posts = Post.objects.all().order_by('-created_on')[:5]
    context = {
        'posts':posts
    }
    return render(request, 'blog.html',context)

class BlogListView(ListView):
    model = Post
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        posts = Post.objects.all().order_by('-created_on')[:5]
        context = super().get_context_data(**kwargs)
        context['posts'] = posts
        return context

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
