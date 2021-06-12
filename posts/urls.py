from django.urls import path
from .views import HomeView, PostDetailView, SportCategoryView, ScienceCategoryView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('sport/', SportCategoryView.as_view(), name="sport"),
    path('science/', ScienceCategoryView.as_view(), name = "science"),
    path('post/<slug:slug>/', PostDetailView.as_view(), name="post")
]
