from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from .forms import BlogPostForm


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/post_form.html'
    form_class = BlogPostForm
    success_url = reverse_lazy('blog:post_list')


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/post_form.html'
    form_class = BlogPostForm
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('blog:post_list')


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/post_delete_confirm.html'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('blog:post_list')