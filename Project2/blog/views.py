"""
from django.shortcuts import render
from django.http import Http404
from blog.models import Post


# Create your views here.

def list(request):
    Data = {
        'Posts': Post.objects.all().order_by("-date")[:10],
    }
    return render(request, 'blog/blog.html', Data)


def post(request, post_id):
    # lấy 1 bài viết có pk = post_id
    # return render(request, 'blog/post.html', {'post': Post.objects.get(pk=post_id)})
    try:
        Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Bài viết không tồn tại nhé!!")
    return render(request, 'blog/post.html', {'post': Post.objects.get(pk=post_id)})


from django.views import generic
from .models import Post


class List(generic.ListView):
    template_name = 'blog/blog.html'
    context_object_name = 'Posts'

    def get_queryset(self):
        return Post.objects.all().order_by("-date")[:10]


class Detail(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'
"""
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from django.http import HttpResponse, HttpResponseRedirect
from home.forms import *


def post(request, pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        post = get_object_or_404(Post, pk=pk)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return HttpResponseRedirect(pk)
    form = CommentForm()
    return render(request, "blog/post.html", {'post': Post.objects.get(pk=pk), 'form': form})
