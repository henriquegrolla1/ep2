from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Post


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
        post_title = request.POST['title']
        post_content = request.POST['content']
        post_date = request.POST['date']
        post = Post(title=post_title,
                    content=post_content,
                    date=post_date)
        post.save()
        return HttpResponseRedirect(
            reverse('blog:detail', args=(post.id, )))
    else:
        return render(request, 'blog/create.html', {})


def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.date = request.POST['date']
        post.save()
        return HttpResponseRedirect(
            reverse('blog:detail', args=(post.id, )))

    context = {'post': post}
    return render(request, 'blog/update.html', context)


def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('blog:index'))

    context = {'post': post}
    return render(request, 'blog/delete.html', context)
