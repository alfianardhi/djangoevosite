from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    thumbnail = models.ImageField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return self.title

class Comment(models.Model):
    author_comment = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.author