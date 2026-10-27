from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Post, Comment, Category
from .forms import PostForm, CommentForm


class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = ['-date']


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_list'] = self.object.comment_set.order_by('-date')
        return context


class PostCreateView(generic.CreateView):
    model = Post
    template_name = 'blog/create.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse('blog:detail', args=(self.object.id, ))


class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = 'blog/update.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse('blog:detail', args=(self.object.id, ))


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog:index')


@login_required
def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = request.user
            comment_text = form.cleaned_data['text']
            comment = Comment(author=comment_author,
                              text=comment_text,
                              post=post)
            comment.save()
            return HttpResponseRedirect(
                reverse('blog:detail', args=(post_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'post': post}
    return render(request, 'blog/comment.html', context)


class CategoryListView(generic.ListView):
    model = Category
    template_name = 'blog/categories.html'
    ordering = ['name']


def detail_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    post_list = category.posts.order_by('-date')
    context = {'category': category, 'post_list': post_list}
    return render(request, 'blog/index.html', context)
