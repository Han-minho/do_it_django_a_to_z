from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Post


# Create your views here.

class PostList(ListView):
    model = Post


def index(request):
    posts = Post.objects.all()

    return render(
        request,'blog/index.html',
        {
            'posts':posts,
        }
    )