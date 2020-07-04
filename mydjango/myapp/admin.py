from django.contrib import admin
from .models import Author, Category, Post, Comment

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
