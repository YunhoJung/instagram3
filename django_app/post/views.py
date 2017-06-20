from django.shortcuts import render, redirect

from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post:post_list', context=context)


def post_detail(request):
    pass


def post_create(request):
    pass


def post_delete(request, post_pk):
    if request == "POST":
        post = Post.Objects.get(pk=post_pk)
        post.delete()
    return redirect('post:post_list')

def post_modify(request)
