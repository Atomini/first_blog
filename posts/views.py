from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.
from .forms import AddPostForm
from .models import BlogPosts


class HomeView(ListView):
    model = BlogPosts
    template_name = "home.html"
    paginate_by = 3

    def get_queryset(self):
        post = BlogPosts.objects.filter(published=True, moderated=True)
        return post.order_by("-published_time")


class PostDetailView(DetailView):
    model = BlogPosts
    template_name = "blogposts_detail.html"
    slug_field = "post_slug"


class CategoryView(ListView):
    model = BlogPosts
    template_name = "home.html"
    paginate_by = 3

    def get_queryset(self):
        posts = BlogPosts.objects.filter(category=self.kwargs['category_slug'], published=True, moderated=True)
        return posts.order_by("-published_time")


class AddPage(CreateView):
    model = BlogPosts
    form_class = AddPostForm
    template_name = "add_page.html"
