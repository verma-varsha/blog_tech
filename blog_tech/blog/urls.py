from django.conf.urls import url
from .views import (
     index,
     post_detail,
     #category_detail,
	)

urlpatterns=[
url(r'^$', index, name='index'),
url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
#url(r'^category/(?P<slug>[\w-]+)/$', category_detail, name='category'),
]