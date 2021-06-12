from django.contrib import admin
from posts.models import BlogPosts, Author, Comments


@admin.register(BlogPosts)
class AdminPost(admin.ModelAdmin):
    prepopulated_fields = {"post_slug": ("title",)}


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    prepopulated_fields = {"author_slug": ("author_name",)}


admin.site.register(Comments)
