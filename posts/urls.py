from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('post/<slug:slug>/', PostDetailView.as_view(), name="post"),
    path('<slug:category_slug>/', CategoryView.as_view(), name="category")
]
