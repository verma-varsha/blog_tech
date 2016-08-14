from django.shortcuts import render
from .models import Post, Category, CommentUser

# Create your views here.

def index(request):
	categories=Category.objects.all()
	latest_post_list=Post.objects.all().order_by('-timestamp')[:5]
	posts=Post.objects.all()
	for p in posts:
		p.post_content_short=p.post_content[0:100]
		#print p.post_content_short
	context={
	   "categories":categories,
	   "latest_post_list":latest_post_list,
	   "posts":posts,
	}
	#print latest_post_list
	return render(request, "index.html", context)