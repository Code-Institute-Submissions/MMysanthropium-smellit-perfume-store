from django.views.generic import (
        ListView, DetailView, CreateView, UpdateView, DeleteView
        )
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class PostList(ListView):
    model = Post
    template_name = 'blog.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'body']


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog')
