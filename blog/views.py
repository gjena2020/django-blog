from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .forms import BlogForm
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


@login_required
def createBlog(request):
    form = BlogForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('blog:home')
    return render(request, 'blog_create.html', {'form':form})

class BlogUpdationView(UpdateView):
    template_name = 'blog_update.html'
    form_class = BlogForm
    model = Blog
    # success_url = reverse_lazy('blog:detail')

class BlogListView(ListView):
    template_name = 'Blog_list.html'
    model = Blog

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'

class BlogDeleteView(DeleteView):
    template_name = 'blog_delete.html'
    model = Blog
    success_url = reverse_lazy('blog:home')