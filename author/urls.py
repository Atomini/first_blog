from django.urls import path
from .views import *

urlpatterns = [
    path('register/', AuthorRegisterView.as_view(), name='register')
]
