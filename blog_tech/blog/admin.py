from django.contrib import admin

# Register your models here.
from .models import Post, Tag, CommentUser

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('post_title',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('tag_title',)}	

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(CommentUser)