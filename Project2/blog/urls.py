from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from .models import Post

urlpatterns = [
    # url(r'^$', views.List.as_view(), name="list"),
    # blog/id
    # url(r'^(?P<post_id>\d+)$', views.post, name="post")
    # url(r'^(?P<pk>\d+)$', views.Detail.as_view(), name="post")
    url(r'^$', ListView.as_view(
        template_name='blog/blog.html',
        queryset=Post.objects.all().order_by("-date")[:10],
        context_object_name="Posts"
    )),
    url(r'^(?P<pk>\d+)$', views.post, name='post'),
]
