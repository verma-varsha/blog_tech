from django.contrib import admin

# Register your models here.
from .models import Post, Category, CommentUser

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(CommentUser)