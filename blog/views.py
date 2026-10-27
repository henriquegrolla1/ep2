from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Post
from .forms import PostForm


def list_posts(request):
    post_list = Post.objects.order_by('-date')
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def detail_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post_title = form.cleaned_data['title']
            post_content = form.cleaned_data['content']
            post_date = form.cleaned_data['date']
            post = Post(title=post_title,
                        content=post_content,
                        date=post_date)
            post.save()
            return HttpResponseRedirect(
                reverse('blog:detail', args=(post.id, )))
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'blog/create.html', context)


def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.date = form.cleaned_data['date']
            post.save()
            return HttpResponseRedirect(
                reverse('blog:detail', args=(post.id, )))
    else:
        form = PostForm(
            initial={
                'title': post.title,
                'content': post.content,
                'date': post.date,
            })

    context = {'post': post, 'form': form}
    return render(request, 'blog/update.html', context)


def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('blog:index'))

    context = {'post': post}
    return render(request, 'blog/delete.html', context)
