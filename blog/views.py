from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import BlogForm
from .models import Blog




class BlogCreateView(LoginRequiredMixin, CreateView):
    form_class = BlogForm
    template_name = 'blog_create.html'
    model = Blog


class BlogUpdationView(LoginRequiredMixin,  UpdateView):
    template_name = 'blog_update.html'
    form_class = BlogForm
    model = Blog

class BlogListView(ListView):
    template_name = 'Blog_list.html'
    model = Blog

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'blog_delete.html'
    model = Blog
    success_url = reverse_lazy('blog:home')