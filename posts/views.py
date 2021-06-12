from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.
from .models import BlogPosts


class HomeView(ListView):
    model = BlogPosts
    template_name = "home.html"
    paginate_by = 10
    ordering = ["-published_time"]


class PostDetailView(DetailView):
    model = BlogPosts
    template_name = "blogposts_detail.html"
    slug_field = "post_slug"


class SportCategoryView(ListView):
    model = BlogPosts
    template_name = "sport_catalog_list.html"
    paginate_by = 10

    def get_queryset(self):
        posts = BlogPosts.objects.filter(category="sport")
        return posts.order_by("-published_time")


class ScienceCategoryView(ListView):
    model = BlogPosts
    template_name = "science_catalog_list.html"
    paginate_by = 10

    def get_queryset(self):
        posts = BlogPosts.objects.filter(category="science")
        return posts.order_by("-published_time")
