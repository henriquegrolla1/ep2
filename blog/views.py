from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Post
from .forms import PostForm


class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = ['-date']


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'


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
