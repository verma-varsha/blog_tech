from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    category_title=models.CharField(max_length=100)
    def __unicode__(self):
        return self.category_title



class Post(models.Model):
    post_title= models.CharField(max_length=150)
    post_content= models.TextField()
    post_content_short= models.CharField(max_length=100, null=True)
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
    author= models.CharField(max_length=100)
    category=models.ForeignKey(Category)
    def __unicode__(self):
        return self.post_title



class CommentUser(models.Model):
    user_name= models.CharField(max_length=150)
    user_email= models.EmailField(max_length=254)
    user_comment= models.TextField()
    user_post=models.ManyToManyField(Post)
    def __unicode__(self):
        return self.user_name
