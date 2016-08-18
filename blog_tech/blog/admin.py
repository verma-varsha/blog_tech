from django.contrib import admin

# Register your models here.
from .models import Post, Category, CommentUser

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('post_title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('category_title',)}	

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CommentUser)