from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.core.paginator import Paginator

class BlogPageView(ListView):
    model = Post
    template_name = "index.html"
    paginate_by = 2


class BlogDetailView(DetailView):
    model = Post
    template_name = "post.html"