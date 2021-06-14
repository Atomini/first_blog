from django import forms
from django.contrib.auth.models import User

from .models import *


class AddPostForm(forms.ModelForm):

    class Meta:
        model = BlogPosts
        fields = ["title", "category", "into_image", "into_text", "post_text", "author"]
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "category": forms.Select(attrs={'class': 'form-control'}),
            "into_text": forms.Textarea(attrs={'class': 'form-control', "rows": "3"}),

            "post_text": forms.Textarea(attrs={'class': 'form-control', "rows": "20"}),
            "author": forms.TextInput(attrs={'class': 'form-control', "value": "", "id": "current_user",
                                             "type": "hidden"}),
        }
