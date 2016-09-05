from django.shortcuts import render, redirect
from .models import Post, Tag, CommentUser


# Create your views here.

def index(request):

    latest_post_list=Post.objects.all().order_by('-timestamp')[:5]
    posts=Post.objects.all()
    for p in posts:
        p.post_content_short=p.post_content[0:100]
        #print p.post_content_short
    context={
       
       "latest_post_list":latest_post_list,
       "posts":posts,
    }
    #print latest_post_list
    return render(request, "index.html", context)



def post_detail(request, slug):
    if request.method=='POST':
        post=request.POST
        p=Post.objects.get(slug=slug)
        c= CommentUser.objects.create(user_post=p, user_name=post['name'], user_email=post['email'], user_comment=post['comment'])
        '''c.user_name=post['name']
        c.user_email=post['email']
        c.user_comment=post['comment']
        print c.user_comment'''
       
    post=Post.objects.get(slug=slug)
    comments=CommentUser.objects.filter(user_post=post)
    context={
    "comments":comments,
    "post":post,
    }   
    #print comments
    return render(request, "post.html", context)

'''def category_detail(request, slug):
    category=Category.objects.get(slug=slug)
    posts= Post.objects.filter(category=category)
    context={
    "posts":posts,
    "category":category,
    }    
    return render(request, "category.html", context)'''