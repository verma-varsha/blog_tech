from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models

# Create your models here.
class Tag(models.Model):
    tag_title=models.CharField(max_length=100)
    slug=models.SlugField(null=True)
    def save(self, *args, **kwargs):
        self.slug=slugify(self.tag_title)
        super(Tag, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.tag_title



class Post(models.Model):
    post_title= models.CharField(max_length=150)
    post_content= models.TextField()
    post_content_short= models.CharField(max_length=100, null=True)
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
    author= models.CharField(max_length=100)
    tag=models.ManyToManyField(Tag)
    slug=models.SlugField(null=True)
    image=models.FileField(null=True, blank=True)
    def save(self, *args, **kwargs):
        self.slug=slugify(self.post_title)
        super(Post, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.post_title



class CommentUser(models.Model):
    user_name= models.CharField(max_length=150)
    user_email= models.EmailField(max_length=254)
    user_comment= models.TextField()
    user_post=models.ForeignKey(Post, null=True)
    def __unicode__(self):
        return self.user_comment
