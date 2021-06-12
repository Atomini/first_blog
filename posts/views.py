from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.
from .models import BlogPosts


class HomeView(ListView):
    model = BlogPosts
    template_name = "home.html"


class PostDetailView(DetailView):
    model = BlogPosts
    template_name = "blogposts_detail.html"
    slug_field = "post_slug"


